from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from pprint import pformat

# ファイル場所の確認
from langs2ast.java.ast_Java.Java8Lexer import Java8Lexer
from langs2ast.java.ast_Java.Java8Parser import Java8Parser

#from JavaParser import JavaParser
#from JavaLexer import JavaLexer

import ast

class AstProcessor:

    def __init__(self, logging, listener):
        self.logging = logging
        self.logger = logging.getLogger(self.__class__.__name__)
        self.listener = listener

    # ★ポイント２
    def execute(self, input_source):
        fs = FileStream(input_source, encoding="utf-8")
        parser = Java8Parser(CommonTokenStream(Java8Lexer(fs)))
        # print(ast.dump(parser))
        walker = ParseTreeWalker()
        # print(">>", self.listener.root) # 0x000001F8B668AB80>
        walker.walk(self.listener, parser.compilationUnit())
        
        # 以下動作しない？
        # print(">>", self.listener.root) # 0x000001F8B668AB80>
        self.logger.debug('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        print('Display all data extracted by AST. \n' + pformat(self.listener.ast_info, width=160))
        # return self.listener.root
        
        
        return self.listener