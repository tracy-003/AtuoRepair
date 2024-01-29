from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from ast_Java.JavaLexer import JavaLexer
from ast_Java.JavaParser import JavaParser
from pprint import pformat

import ast

class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    def execute(self, input_source):
        fs = FileStream(input_source, encoding="utf-8")
        parser = JavaParser(CommonTokenStream(JavaLexer(fs)))
        # print(ast.dump(parser))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.compilationUnit())
        self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        print('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        return self.listener.ast_info