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
        self.java_ast_body = []
        self.dic_java_type = dict()

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
        # print("tree")
        # (self)listenerを変更する
        
        make_Java_tree.make_Tree(ctx, self)
        # ここまでで終了してる？？？
        # print("tree", tree)
        # print("tree is None", tree is None)
        

        # Node(tree, parent = self.root)
        # show_NewTree(tree)
        # tree.parent = self.root
        # show_NewTree(self.root)
        
        # exit()        
        #print("{0} {1} {2}".format(ctx.start.line, ctx.start.column, ctx.getText()))
        self.call_methods = []

    # Enter a parse tree produced by JavaParser#methodCall.
    """def enterMethodCall(self, ctx):#:Java8Parser.MethodCallContext):
        s = make_Java_tree.make_Tree(ctx) #,  self.ast_tree)
        print("*" * 200)
        print(s)
        print("*" * 200)
        #showTree(ctx)
        # ★ポイント７
        line_number = str(ctx.start.line)
        column_number = str(ctx.start.column)
        ctx_p = ctx.parentCtx
        print("*" * 20)
        print(ctx)
        
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
        self.call_methods.append(line_number + ' ' + column_number + ' ' + parent)"""