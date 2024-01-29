from langs2ast.java.ast_Java.Java8ParserListener import Java8ParserListener
from langs2ast.java.ast_Java.Java8Parser import Java8Parser

from langs2ast.java.ast_Java import make_Java_tree #自作プログラム
from anytree import Node, RenderTree # 木構造
from anytree.exporter import DotExporter

from langs2ast.java.ast_Java import settings

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
        self.f_path = "isfirst.txt"
        self.write_file('0')

    # 木を足す。    
    def addTree(self, parent, tree):
        #print("Add Tree", "=" * 20)
        #print(type(tree))
        for pre, fill, node in RenderTree(tree):
            print(pre, fill, node.name)

    def reverse_bool(self):
        
        exit("basic_info_listener.py 66")

    # ファイルの書き込み
    def write_file(self, number):
        # number
        # 0 → 初期化(True)
        # 1 → False
        f = open(self.f_path, "w")
        f.write(number)
        f.close()

    # ファイルの読み込み
    def read_file(self):
        """f = open(self.f_path, "r")
        str_num = f.read()
        print("str_num", ":::", str_num)
        f.close()"""

        # self.write_file('1')

        f = open(self.f_path, "r")
        str_num = f.read()
        f.close()
        
        # print("str_num", ":::", str_num)
        
        # exit()
        return int(str_num)

    # Enter a parse tree produced by JavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:Java8Parser.MethodDeclarationContext):
        # showTree(ctx)
        # ここで返却された木を追加
        # print("tree")
        # (self)listenerを変更する
        # 宣言文の回数だけ回るみたいなので…
        # print("宣言文に入りました！", self.isfirst)
        
        if self.read_file() == 0:
            make_Java_tree.make_Tree(ctx, self)
            self.write_file('1')
            # exit("Decal2")
        """else:
            exit("Decal")"""
        
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