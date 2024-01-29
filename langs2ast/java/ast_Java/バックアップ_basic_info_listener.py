from ast_Java.Java8ParserListener import Java8ParserListener
from ast_Java.Java8Parser import Java8Parser

from ast_Java import make_Java_tree #自作プログラム
from anytree import Node, RenderTree # 木構造
from anytree.exporter import DotExporter

cnt = 0
tars = [[100],[100],[100],[0,2],[0],[0],[""],[0],[1],[0],[1,2,3],[0],[3]]

def show_NewTree(tree):
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))

def showTree(ctx):
    global cnt
    global tars
    tar = tars.pop()
    #print("カウント！", cnt, tar)
    #tar = tars[cnt]
    # ctx_p = ctx.parentCtx
    num = (len(ctx.children)) # 子どもの数
    # print("ctx_p", type(ctx), ctx.getRuleIndex())
    # print("親",  ctx.parentCtx.getText(), "子",num)
    for i in range(num):
        ctx_p_c = ctx.getChild(i)
        txt = ctx_p_c.getText()
        #print(type(ctx_p_c), end = ",")
        #print(txt)
        #print(i,tar,"ターゲットの部分")
        if i in tar:
            showTree(ctx_p_c)
    cnt += 1
    #print("showTree終わりです。")
     
# ★ポイント３
class BasicInfoListener(Java8ParserListener):

    # ★ポイント４
    def __init__(self, name):
        self.call_methods = []
        self.ast_info = {
            'packageName': '',
            'className': '',
            'implements': [],
            'extends': '',
            'imports': [],
            'fields': [],
            'methods': []
        }
        self.file_name = name
        self.root = Node(self.file_name, parent = None)

    # ★ポイント５
    # Enter a parse tree produced by JavaParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:Java8Parser.PackageDeclarationContext):
        self.ast_info['packageName'] = ctx.qualifiedName().getText()

    # Enter a parse tree produced by JavaParser#importDeclaration.
    def enterImportDeclaration(self, ctx:Java8Parser.ImportDeclarationContext):
        import_class = ctx.qualifiedName().getText()
        self.ast_info['imports'].append(import_class)
    
    # 木を足す。    
    def addTree(self, parent, tree):
        #print("Add Tree", "=" * 20)
        #print(type(tree))
        for pre, fill, node in RenderTree(tree):
            print(pre, fill, node.name)

    

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Java8Parser.MethodDeclarationContext):
        # showTree(ctx)
        # ここで返却された木を追加
        print("*" * 20)
        tree = make_Java_tree.make_Tree(ctx)#, self.ast_tree)
        print("*" * 20)
        # Node(tree, parent = self.root)
        # show_NewTree(tree)
        tree.parent = self.root
        show_NewTree(self.root)
        
        exit()        
        #print("{0} {1} {2}".format(ctx.start.line, ctx.start.column, ctx.getText()))
        self.call_methods = []

    # Enter a parse tree produced by JavaParser#methodCall.
    def enterMethodCall(self, ctx:Java8Parser.MethodCallContext):
        #showTree(ctx)
        # ★ポイント７
        line_number = str(ctx.start.line)
        column_number = str(ctx.start.column)
        ctx_p = ctx.parentCtx
        print("*" * 20)
        print(ctx)
        """
        print("70親：",ctx_p.getText())
        print("71親：",ctx_p.parentCtx.getText())
        print((len(ctx_p.children))) # 子どもの数
        print("ctx_p", type(ctx_p), ctx_p.getRuleIndex())
        ctx_p_c = ctx_p.getChild(0)
        print("ctx_p_c", type(ctx_p_c), ctx_p_c.getText())
        ctx_p_c = ctx_p.getChild(1)
        print("ctx_p_c", type(ctx_p_c), ctx_p_c.getText())
        print("66行目は？？",(ctx_p_c.getChild(0))) # 子どもの数
        ctx_p_c = ctx_p.getChild(2)
        print("ctx_p_c", type(ctx_p_c), ctx_p_c.getText())
        parent = ctx_p.getText()
        print("p", parent)
        self.call_methods.append(line_number + ' ' + column_number + ' ' + parent)
        """

    # Enter a parse tree produced by JavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:Java8Parser.ClassDeclarationContext):
        child_count = int(ctx.getChildCount())
        if child_count == 7:
            # class Foo extends Bar implements Hoge
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            # c3 = ctx.geChild(2)  # ---> extends
            c4 = ctx.getChild(3).getChild(0).getText()  # ---> extends class name
            # c5 = ctx.getChild(4)  # ---> implements
            # c7 = ctx.getChild(6)  # ---> method body
            self.ast_info['className'] = c2
            self.ast_info['implements'] = self.parse_implements_block(ctx.getChild(5))
            self.ast_info['extends'] = c4
        elif child_count == 5:
            # class Foo extends Bar
            # or
            # class Foo implements Hoge
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            c3 = ctx.getChild(2).getText()  # ---> extends or implements

            # c5 = ctx.getChild(4)  # ---> method body
            self.ast_info['className'] = c2
            if c3 == 'implements':
                self.ast_info['implements'] = self.parse_implements_block(ctx.getChild(3))
            elif c3 == 'extends':
                c4 = ctx.getChild(3).getChild(0).getText()  # ---> extends class name or implements class name
                self.ast_info['extends'] = c4
        elif child_count == 3:
            # class Foo
            # c1 = ctx.getChild(0)  # ---> class
            c2 = ctx.getChild(1).getText()  # ---> class name
            # c3 = ctx.getChild(2)  # ---> method body
            self.ast_info['className'] = c2

    # Enter a parse tree produced by JavaParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:Java8Parser.FieldDeclarationContext):
        field = {
            'fieldType': ctx.getChild(0).getText(),
            'fieldDefinition': ctx.getChild(1).getText()
        }
        self.ast_info['fields'].append(field)

    def parse_implements_block(self, ctx):
        implements_child_count = int(ctx.getChildCount())
        result = []
        if implements_child_count == 1:
            impl_class = ctx.getChild(0).getText()
            result.append(impl_class)
        elif implements_child_count > 1:
            for i in range(implements_child_count):
                if i % 2 == 0:
                    impl_class = ctx.getChild(i).getText()
                    result.append(impl_class)
        return result

    def parse_method_params_block(self, ctx):
        params_exist_check = int(ctx.getChildCount())
        result = []
        # () ---> 2
        # (Foo foo) ---> 3
        # (Foo foo, Bar bar) ---> 3
        # (Foo foo, Bar bar, int count) ---> 3
        if params_exist_check == 3:
            params_child_count = int(ctx.getChild(1).getChildCount())
            if params_child_count == 1:
                param_type = ctx.getChild(1).getChild(0).getChild(0).getText()
                param_name = ctx.getChild(1).getChild(0).getChild(1).getText()
                param_info = {
                    'paramType': param_type,
                    'paramName': param_name
                }
                result.append(param_info)
            elif params_child_count > 1:
                for i in range(params_child_count):
                    if i % 2 == 0:
                        param_type = ctx.getChild(1).getChild(i).getChild(0).getText()
                        param_name = ctx.getChild(1).getChild(i).getChild(1).getText()
                        param_info = {
                            'paramType': param_type,
                            'paramName': param_name
                        }
                        result.append(param_info)
        return result