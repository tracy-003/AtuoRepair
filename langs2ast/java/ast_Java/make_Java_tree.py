from langs2ast.java import Java2ast00
from langs2ast.java import ast_Java

from langs2ast.java.ast_Java.Java8ParserListener import Java8ParserListener
from langs2ast.java.ast_Java.Java8Parser import Java8Parser

from langs2ast.java import makeAST_JavaExpr

from langs2ast.java.ast_Java.Return_Words import Return_Words


import antlr4
import sys
from anytree import Node, RenderTree

# from ast_Java import Java2ast00

# これらは使われていない？？
# from trans.make_middle.Java2ast00 import return_input, return_input_int
# from Java2ast00 import return_input, return_input_int

def add_parent(node_child, node_parent):
    # 第1引数：子ども（した）
    # 第2引数：親（うえ）
    # 子どもが存在するときに、枝をつける
    if node_child is not None:
        node_child.parent = node_parent
    return node_parent

# 子どもの数を返却。無かったら0を返す。


def return_children_number(parent):
    try:
        num = len(parent.children)
    except AttributeError:  # 子を持っていないとき
        num = 0
    return num


def show_NewTree(tree):
    # pass
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))


"""
class tree_secntence:
    def __init__(self):
        # self.
"""


def make_tree_BSC(ctx, listener):
    return_tree = ""
    num_child = return_children_number(ctx)
    # print(num_child)
    # exit()
    # 子が1人：BlockContext
    if num_child == 1:
        # print(type(ctx.getChild(0)))
        # print(listener, "\n listenerのエラーです")
        return_tree = return_sentence_tree(ctx.getChild(0), listener)
        # print(return_tree)
        # exit()
        
    # 子が複数
    else:
        return_tree = Node("type_ast_BSC", parent=None)
        for i in range(num_child):
            # txt = ctx.getChild(i).getText()
            # Node(txt, parent = return_tree)
            child_BSC = ctx.getChild(i)
            tree = return_sentence_tree(child_BSC, listener)
            return_tree = add_parent(tree, return_tree)

    return return_tree

# ast_Java.Java8Parser.Java8Parser.StatementContext の型
def make_tree_SC(ctx, listener = None):
    # ast_Java.Java8Parser.Java8Parser.StatementContext
    num_child = return_children_number(ctx)
    # return_tree = Node("type_ast_SC", parent=None)
    # 子が1人：
    child = None
    if num_child == 1:
        child = ctx.getChild(0)
        print("83", child.getText(), type(child))
        
    else:
        print("make_Java_tree.py のmake_tree_SC()の子が複数の場合は未実装です。")
        for i in range(num_child):
            print(i,ctx.getChild(i).getText())
        exit(1)
    
    print("91", child.getText(), type(child))
    ast_obj = return_sentence_tree(child, listener)
    print(ast_obj)
    # exit("93行目")
    
    if listener is None:
        return ast_obj
    
    else:
        # print(listener)
        listener.java_ast_body.append(ast_obj)
        print("ここは未実装です。", "make_Java_tree.py", ">>", ast_obj, type(child))
        # exit(1)
    # child_tree = return_sentence_tree(child, listener)
    # print("子供の木", child_tree)
    # if child_tree is not None:
    #     child_tree.parent = return_tree
    
    #for i in range(num_child):
        # txt = child.getText()
        # ここを変更
        # child_tree = return_sentence_tree(child, listener)
        # child_tree.parent = return_tree
        # Node(txt, parent = return_tree)
        # return_tree = add_parent(tree, return_tree)
    # show_NewTree(return_tree)
    # return return_tree

# 木を見て変数名を返却する


def return_sys(ctx, listener = None):
    num = return_children_number(ctx)
    
    # while type(ctx) is ast_Java.Java8Parser.Java8Parser.StatementExpressionContext:
    
    while type(ctx) is ast_Java.Java8Parser.Java8Parser.MethodInvocationContext or num == 1:
        # 子供は1人
        ctx = ctx.getChild(0)
        num = return_children_number(ctx)
        for j in range(num):
            chi = ctx.getChild(j)
            print(j, type(chi))
            if ctx is not None:
                print(j, chi.getText())
            else:
                print("None")
    print("==" * 20)
    
    # System系？？？               
    # ast_Java.Java8Parser.Java8Parser.StatementExpressionContext
    sys_c_c = ctx.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.StatementWithoutTrailingSubstatementContext
    sys_c = sys_c_c.getChild(0)

    print("sys_c_c", sys_c_c.getText())
    print("sys_c", sys_c.getText())

    #print(return_children_number(sys_c))
    # for i in range(return_children_number(sys_c)):
        # 0 System.out <class 'ast_Java.Java8Parser.Java8Parser.TypeNameContext'>
        # 1 . <class 'antlr4.tree.Tree.TerminalNodeImpl'>
        # 2 println <class 'antlr4.tree.Tree.TerminalNodeImpl'>
        # 3 ( <class 'antlr4.tree.Tree.TerminalNodeImpl'>
        # 4 "YES" <class 'ast_Java.Java8Parser.Java8Parser.ArgumentListContext'>
        # 5 ) <class 'antlr4.tree.Tree.TerminalNodeImpl'>
        
        # print(i,sys_c.getChild(i).getText(), type(sys_c.getChild(i)))
    
    if sys_c is None:
        print("sys_cはNoneです。")
        print("make_Java_tree.py", ">>", "return_sys()")
        print("sys_c_c", sys_c_c.getText())
        return ""
        # exit(1)
    
    else:
        ast_p = None
        # System系かどうかの確認
        
        txt_sys_c = sys_c.getText()
        name_hensu = sys_c.getChild(0).getText()
        if name_hensu == "System.out":
            # ここには実値だけでなく、計算式も入っている可能性がある。
            arg = sys_c.getChild(4)
            # ここで、改行が含まれているかどうかを確認する。
            isNoN = False
            if "println" in name_hensu:
                pass
            else:
                # 改行がない場合、True
                isNoN = True
            ast_p = Java2ast00.return_print(arg, isNoN)
            #print("+"*20)
            #print(ast_p)
            # import astunparse
            # print(astunparse.unparse(ast_p))
        
        # 標準の代入
        elif  "=" in txt_sys_c:
            if "nextInt()" in sys_c.getText():
                ast_p = Java2ast00.return_Assign(
                    name_hensu, # 変数名
                    Java2ast00.return_input_int()
                )
            # int以外の代入
            # += とかあるやん！
            elif "=" in txt_sys_c:
                print("代入しましょ！！")
                print(name_hensu)
                print(sys_c.getChild(1).getText())
                print(sys_c.getChild(2).getText())
                # print(sys_c.getText())
                # exit()
                
                as_eq_type = sys_c.getChild(1).getText()
                if as_eq_type == "=":
                    ast_p = Java2ast00.return_Assign(
                        name_hensu, # 変数名
                        sys_c.getChild(2).getText() # 変数値
                    )
                elif as_eq_type == "+=":
                    ast_p = Java2ast00.return_AugAssign(
                        name_hensu, # 変数名
                        sys_c.getChild(1).getText(), # 演算子
                        sys_c.getChild(2).getText() # 変数値
                    )
                else:
                    exit("代入方法が未定です。 make_Java_tree.py")


        
        if ast_p is None:
            print(sys_c.getText())
            print(sys_c.getChild(0), sys_c.getChild(0).getText())
            
            print("222:make_Java_tree.py", ">>", "return_sys()")
            exit(str(r"C:\Users\user\new_study\trans\make_middle\ast_Java\make_Java_tree.py") + "：ast_pがNoneです。")
        
        """
        if type(sys_c) is ast_Java.Java8Parser.Java8Parser.StatementExpressionContext:
            print(ctx.getText(), return_children_number(sys_c))
            
        
        for i in range(num):
            print(i,ctx.getChild(i).getText(), type(ctx.getChild(i)))
            
        print(type(ctx), ctx.getText())
        """            
        # exit()
        # Noneのとき、ast自体の返却
        # print("lis",listener)
        # exit()
        if listener is None:
            import ast
            print("ast_p", ast.dump(ast_p))
            return ast_p

        # 本体のとき
        else:
            # print(listener.java_ast_body)
            listener.java_ast_body.append(ast_p)
            # エラーが起きるため、返却
            # return ""
            # exit(str(r"C:\Users\user\new_study\trans\make_middle\ast_Java\make_Java_tree.py") + "：listerに要素があります。：236")
            return ast_p

            

# 呼び出されるのがメインだけとは限らない。
# listerがNoneのときはModule全体ではなく、一部のASTを返却する
def return_sentence_tree(ctx, listener = None):
    return_tree = None # "def return_sentence_tree(ctx):"
    type_tree = type(ctx)
    print("260 ",type_tree, "です")
    # print("-" * 20)
    # print(type_tree, ctx.getText())
    # print("-" * 20)
    num_child = return_children_number(ctx)
    # BlockStatementContextの場合
    # そのまま代入文 or BlockContext(子が1つ)へ
    if type_tree == ast_Java.Java8Parser.Java8Parser.BlockStatementContext:
        print("201 >>", return_tree)
        return_tree = make_tree_BSC(ctx, listener)
        print("203 >>", return_tree)
        # exit()

    elif type_tree == ast_Java.Java8Parser.Java8Parser.StatementContext:
        ctx = ctx.getChild(0)
        print("ここです１", type(ctx))
        return_tree = return_sentence_tree(ctx, listener)
        # print("|||||||||||||||||||||||||||||||||||||||||||||||")
        print(ctx.getText())
        print("return_tree", return_tree)
        return return_tree
        # exit()
        # return_tree = make_tree_SC(ctx, listener)

    elif type_tree == ast_Java.Java8Parser.Java8Parser.ExpressionContext:
        # System系
        # System.out.println(s)
        # System.out.print(s)
        # System.out
	    # System
        # print(">" * 100)
        # print(ctx.getText())
        print("system系" * 6)
        return_tree = Node("system系", parent=None)
        return return_tree

    elif type_tree == antlr4.tree.Tree.TerminalNodeImpl:
        # 記号系
        # print("記号系", ">" * 20, ctx.getText())
        pass

    elif type_tree == ast_Java.Java8Parser.Java8Parser.LocalVariableDeclarationContext:
        # String s = "Test" ⇒ 代入部分
        print(return_tree)
        print("make_Java_tree.py 307 type_tree == ast_Java.Java8Parser.Java8Parser.LocalVariableDeclarationContext")
        exit()
    
    
    
    elif type_tree == ast_Java.Java8Parser.Java8Parser.LocalVariableDeclarationStatementContext:
    # elif ast_Java.Java8Parser.Java8Parser.LocalVariableDeclarationStatementContext:
        # (1)　代入の時
        # ctx
        # 0 Scannersc=newScanner(System.in)
        # 1 ;
        ctx = ctx.getChild(0)
        num = return_children_number(ctx)
        print(str(r"C:\Users\user\new_study\trans\make_middle\ast_Java\make_Java_tree.py") , 282, "行目")
        print("283 ctxの表示：", ctx.getText())
        # 0：型
        name_type = ctx.getChild(0)
        # print(name_type.getText(), ant_as.getText())
        # print("型", name_type.getText(), type(name_type))
        # if name_type
        # 1：変数名と代入する値
        # ast_Java.Java8Parser.Java8Parser.VariableDeclaratorContext
        ant_as = ctx.getChild(1)
        # ant_asは子供は1人
        ant_as = ant_as.getChild(0)
        # 上のant_asは子供は3人
        # 0：変数名
        # 1：=
        # 2：代入する値
        # スキャナ型の時のみ変数名がスキャナとして保存してスキップ
        if name_type.getText() == "Scanner":
            print("300行目", listener.dic_java_type)
            listener.dic_java_type[ant_as.getChild(0).getText()] = "Scanner"
            print("302行目",listener.dic_java_type)
            return Java2ast00.return_input()
                 
        # スキャナー型以外の普通の代入
        else:
            print("307行目", ant_as.getText(), "この型は", name_type.getText() , "です。")
            #for i in range(num):
            #    print(i, ctx.getChild(i).getText(), type(ctx.getChild(i)))
            ant_name = ant_as.getChild(0).getText()
            
            num_chi = return_children_number(ant_as)
            ant_val = None
            # 子供の数が1のとき：String s; など宣言のみになっている！
            if num_chi == 1:
                # pythonだとできないので、初期値を与えてあげる！
                # やっぱり、Noneを与えたほうがいいみたい
                # ：https://chaika.hatenablog.com/entry/2018/08/17/173044
                # 「python 初期化なし」の検索結果
                ant_val = None

            else:
                ant_val = str(ant_as.getChild(2).getText())
                # 型によって代入する値を変える '3'→3
                if name_type.getText() == "int":
                    if ant_val.isdecimal():
                        ant_val = int(ant_val)
                
            print(str(r"C:\Users\user\new_study\trans\make_middle\ast_Java\make_Java_tree.py"), 317)
            tree = Java2ast00.return_Assign(ant_name, ant_val)
            # listerがNoneのときはModule全体ではないので、return
            if listener is None:
                return tree
            # それ以外の時、全体に追加して返却
            else:
                listener.java_ast_body.append(tree)
            
            
        # exit()
        # return_tree = Node("代入ノード")
        
    
    # elseが無いとき
    elif type_tree == ast_Java.Java8Parser.Java8Parser.IfThenStatementContext:
        return_tree = return_ast_if(ctx)
        if listener is not None:
            listener.java_ast_body.append(return_tree)
        return return_tree

    # elseがあるとき
    elif type_tree == ast_Java.Java8Parser.Java8Parser.IfThenElseStatementContext:
        print("+++++++++++++++++++++++++++++++++++++")
        # print(ctx.getText())
        
        # 構文木をastに直す
        return_tree = return_ast_if(ctx)
        # リスナーがある場合
        if listener is not None:
            # astをjava_ast_bodyに追加
            listener.java_ast_body.append(return_tree)
        else:
            return return_tree
        # return_tree = Node("ifブロックノード")
    
    elif type_tree == ast_Java.Java8Parser.Java8Parser.StatementWithoutTrailingSubstatementContext:
        # これがシステムだけじゃない！！
        # 0 {inttest=0;} <class 'ast_Java.Java8Parser.Java8Parser.BlockContext'>
        # 0 System.out.println("YES"); <class 'ast_Java.Java8Parser.Java8Parser.ExpressionStatementContext'>
        num = return_children_number(ctx)
        if num != 1:
            print("子の数が1じゃない")
            print("make_Java_tree.py", num, ctx.getText(), type(ctx))
            
        # for i in range(num):
        #    print(i, ctx.getChild(i).getText(), type(ctx.getChild(i)))
        # exit()
        else:
            type_child = type(ctx.getChild(0))
            # 多分システム系
            if type_child is ast_Java.Java8Parser.Java8Parser.ExpressionStatementContext:
                # {inttest=0;}
                # print("ブロック")
                # print(ctx.getChild(0).getText())
                # print(type(ctx.getChild(0)))
                # exit()
                return return_sys(ctx, listener)
            
            # 代入系
            elif type_child is ast_Java.Java8Parser.Java8Parser.BlockContext:
                # type_child 
                ctx = ctx.getChild(0)
                # print(return_children_number(ctx))
                print(ctx.getText(), type(ctx))
                print(type_child)
                print(type(ctx) is type_child)
                num = return_children_number(ctx)
                
                for i in range(num):
                    print(i, ctx.getChild(i).getText(), type(ctx.getChild(i)))
                    # 0 { <class 'antlr4.tree.Tree.TerminalNodeImpl'>
                    # 1 inttest=0; <class 'ast_Java.Java8Parser.Java8Parser.BlockStatementsContext'>
                    #                      ast_Java.Java8Parser.Java8Parser.BlockStatementsContext
                    # 2 } <class 'antlr4.tree.Tree.TerminalNodeImpl'>
                body_BSC = ctx.getChild(1)
                
                ast_body = return_sentence_tree(body_BSC, listener)
                # print(body.getText(), type(body))
                print(ast_body)
                # import ast
                # print(ast.dump(ast_body))
                # exit()
                return ast_body
                
            elif type_child is ast_Java.Java8Parser.Java8Parser.ReturnStatementContext:
                return Java2ast00.return_return()

            else:
                print("この型は未実装です。", type_child)
                print("make_Java_tree.py", num, ctx.getText(), type(ctx))
                
        
    elif type_tree == ast_Java.Java8Parser.Java8Parser.ExpressionStatementContext:
        # exit()
        print(ctx.getText())
        return return_sys(ctx, listener)
    
    elif type_tree == ast_Java.Java8Parser.Java8Parser.BlockStatementsContext:
        # print(ctx.getText())
        # print(type(ctx))
        # print(return_children_number(ctx))
        # exit()
        num = return_children_number(ctx)
        
        if num == 1:
            return return_sentence_tree(ctx.getChild(0), listener)
        
        else:
            print("子の数が1じゃない")
            print("make_Java_tree.py", num, ctx.getText(), type(ctx))
            listA = []
            for i in range(num):
                print(i, ctx.getChild(i).getText(), type(ctx.getChild(i)))
                listA.append(return_sentence_tree(ctx.getChild(i)))
            print("listAの表示",listA)
            return listA
            # exit()
    
    # while文の更新
    elif type_tree == ast_Java.Java8Parser.Java8Parser.WhileStatementContext:
        print("親:", ctx.getText ())
        num = return_children_number(ctx)
        """for i in range(num):
            chi = ctx.getChild(i)
            print(i,type(chi), chi.getText())
        """
        # 親: while(1000>Y||Y>2999){Y=scan.nextInt();}
        # 0 <class 'antlr4.tree.Tree.TerminalNodeImpl'> while
        # 1 <class 'antlr4.tree.Tree.TerminalNodeImpl'> (
        # 2 <class 'ast_Java.Java8Parser.Java8Parser.ExpressionContext'> 1000>Y||Y>2999
        # 3 <class 'antlr4.tree.Tree.TerminalNodeImpl'> )
        # 4 <class 'ast_Java.Java8Parser.Java8Parser.StatementContext'> {Y=scan.nextInt();}
        import ast
        # 返却する大元を作成
        ast_while = ast.While()
        # 条件式を設定
        while_expr_list = make_word_list_Main(ctx.getChild(2))
        print(makeAST_JavaExpr.Main(while_expr_list))
        ast_while.test = makeAST_JavaExpr.Main(while_expr_list).return_astTree()
        
        ast_while.body = []
        block4 = ctx.getChild(4)
        # 4 <class 'ast_Java.Java8Parser.Java8Parser.StatementContext'> {Y=scan.nextInt();}
        if type(block4) is not ast_Java.Java8Parser.Java8Parser.StatementContext:
            exit("予想外の構文です。 make_Java_tree.py 507 >>" + str(type(block4)))
        else:
            pass
        
        block4 = block4.getChild(0).getChild(0)
        block4 = block4.getChild(1)

        # whileの中身
        n = return_children_number(block4)
        for i in range(n):
            # print(i, block4.getChild(i).getText())
            c = return_sentence_tree(block4.getChild(i))
            print(c)#, c.getText(), type(c))
            
            ast_while.body.append(return_sentence_tree(block4.getChild(i)))


        
        ast_while.orelse = []

        # print("作成したastオブジェクトの表示")
        # print(ast.dump(ast_while))
        # import astunparse
        # print(astunparse.unparse(ast_while))        
        # exit("exit::496")
        listener.java_ast_body.append(ast_while)
        # print(listener.java_ast_body)
        
        return ast_while




        


        


        
    
    else:
        # エラー出力
        print('以下のクラスは対応していません。', file=sys.stderr)
        print(type_tree, file=sys.stderr)
        print(">>", ctx.getText(), file=sys.stderr)

        import Send_Mail
        print("=" * 1000)
        Send_Mail.send_message("システム強制終了のお知らせ", "Javaを変換できません。 このクラスに未対応です：" + ctx.getText())
        print("=" * 1000)

        sys.exit(1)

    """
    # ctx = ctx.getChild(0)
    print(">" * 10,type(ctx), ctx.getText())
    """
    return return_tree

# 記号系のastを返却する。
def return_ast_symbol(ctx):
    if type(ctx) == antlr4.tree.Tree.TerminalNodeImpl:
        print("記号系")
        ast_obj = Java2ast00.return_symbol(ctx.getText())

def me(ctx):
    num = return_children_number(ctx)
    #while num != 1:
    # print(ctx.getText())
    for i in range(num):
        chi = ctx.getChild(i)
        print(i, str(chi.getText()), type(chi))
        me(chi)

def return_ast_if(ctx):
    """me(ctx)
    # 自作モジュールの使用           
    print("if文について")
    for i in range(return_children_number(ctx)):
        chi = ctx.getChild(i)
        print(i, type(chi), str(chi.getText()))"""

    num = return_children_number(ctx)
    for i in range(num):
        print(i, type(ctx.getChild(i)),ctx.getChild(i).getText())
    # exit()
    """
    0 <class 'antlr4.tree.Tree.TerminalNodeImpl'> if
    1 <class 'antlr4.tree.Tree.TerminalNodeImpl'> (
    2 <class 'ast_Java.Java8Parser.Java8Parser.ExpressionContext'> y%400==0
    3 <class 'antlr4.tree.Tree.TerminalNodeImpl'> )
    4 <class 'ast_Java.Java8Parser.Java8Parser.StatementNoShortIfContext'> {System.out.println("YES");inttest=0;}
    5 <class 'antlr4.tree.Tree.TerminalNodeImpl'> else
    6 <class 'ast_Java.Java8Parser.Java8Parser.StatementContext'> if(y%100==0)System.out.println("NO");elseif(y%4==0)System.out.println("YES");
    """

    
    # if文の条件式をastにする
    print("条件")
    # 2で取得したときは、 <class 'ast_Java.Java8Parser.Java8Parser.AssignmentExpressionContext'>
    class_return_words = Return_Words()
    class_return_words.make_list(ctx.getChild(2))
    word_list = class_return_words.get_words()
    print(word_list)
    
    
    java_expr_obj = makeAST_JavaExpr.Main(word_list)
    ast_tar_expr = java_expr_obj.return_astTree()
    print(ast_tar_expr)
    import astunparse
    import ast
    # print(ast.dump(ast_expr))
    
    """# print(word_list)
    print("[")
    for t in word_list:
        print(t)
    print("]")
    """
    
    
    
    # exit()
    """
    # その後、0で取得ast_Java.Java8Parser.Java8Parser.ConditionalExpressionContext
    if_express = ctx.getChild(2).getChild(0)
    # 以下で得られるのは、ast_Java.Java8Parser.Java8Parser.ConditionalOrExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.ConditionalAndExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.InclusiveOrExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.ExclusiveOrExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.AndExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.EqualityExpressionContext
    if_express = if_express.getChild(0)
    # ast_Java.Java8Parser.Java8Parser.EqualityExpressionContext
    if_express = if_express.getChild(0)
    
    for i in range(return_children_number(if_express)):
        # 0 <class 'ast_Java.Java8Parser.Java8Parser.EqualityExpressionContext'> a%2
        # 1 <class 'antlr4.tree.Tree.TerminalNodeImpl'> ==
        # 2 <class 'ast_Java.Java8Parser.Java8Parser.RelationalExpressionContext'> 0
        print(i, type(if_express.getChild(i)), if_express.getChild(i).getText())
        i = return_children_number(if_express)
    """
    import ast    
    import astunparse
    # 条件式のastを作成
    ast_target = ast.If()
    # ast_target.test = ast.Constant(value = True, kind = None)
    # ast_target.test = ast.Compare(left=ast.BinOp(left=ast.Name(id='a', ctx=ast.Load()), op=ast.Mod(), right=ast.Constant(value=2, kind=None)))
    # ast_target.test.ops = [ast.Eq()]
    # ast_target.test.comparators=[ast.Constant(value=1, kind=None)]
    # print(ast.dump(ast_target))
    ast_target.test = ast_tar_expr
    # if文
    # 真のときのastを作成
    ast_target.body = []
    # これでBlockContextになる(0,2→括弧、1→文)
    java_ctx_body_all = ctx.getChild(4).getChild(0).getChild(0)
    if type(java_ctx_body_all) is not ast_Java.Java8Parser.Java8Parser.BlockContext:
        print("make_Java_tree.py でIfのボディーのコードがBlockContextではない。", file=sys.stderr)
        print(type(java_ctx_body_all), java_ctx_body_all.getText(), file=sys.stderr)
        # system.out.print系の時
        if type(java_ctx_body_all) is ast_Java.Java8Parser.Java8Parser.ExpressionStatementContext:
        # 一文ずつ解析し、bodyに追加していく
            # print(return_children_number(java_ctx_body_all))
            # print(type(java_ctx_body_all.getChild(0)))
            # exit()
            print("java_ctx_body_allのgetChild(0)に対して", type(java_ctx_body_all.getChild(0)))
            print(java_ctx_body_all.getText())
            obj = return_sentence_tree(java_ctx_body_all)
            print("579行目：",obj)
            ast_target.body.append(obj)
            # exit()
            
        else:
            print("未実装のため、exit()")
            print("make_Java_tree.py でIfのボディーのコードがBlockContextではない。", file=sys.stderr)
            exit(1)
    
    
    else:
        # BlockContextの場合、子供は3つ。0,2は括弧、1が文
        java_ctx_body = java_ctx_body_all.getChild(1)
        for i in range(return_children_number(java_ctx_body)):
            # print(i, type(java_ctx_body.getChild(i)), java_ctx_body.getChild(i).getText())
            # 0 <class 'ast_Java.Java8Parser.Java8Parser.BlockStatementContext'> System.out.println("YES");
            # 1 <class 'ast_Java.Java8Parser.Java8Parser.BlockStatementContext'> inttest=0;
            # 一文ずつ解析し、bodyに追加していく
            ast_sc = return_sentence_tree(java_ctx_body.getChild(i))
            print("629 ast_sc",ast_sc)
            # 真のastを追加する。
            ast_target.body.append(ast_sc)
        
        # exit()
        # print(type(java_ctx_body), java_ctx_body.getText())
    #print(type(java_ctx_body), java_ctx_body.getText())
    #print(return_children_number(java_ctx_body))
    

    # 偽のときのastを作成(これを空にすると、elseを省略できる)
    ast_target.orelse = []
    # elseがある時
    print("elseがありますか？？？？", num > 6, num)
    if num > 6:
        print("orelse")
        print('"-"*20', "-"*20)
        java_ctx__orelse = ctx.getChild(6)
        # print(java_ctx__orelse)
        # print(java_ctx__orelse.getText())
        # exit()
        if java_ctx__orelse.getText() == "":
            print("make_Java_tree.py でIfのorelseのコードがNone。", file=sys.stderr)
            #exit(1)
        #print(type(java_ctx__orelse), java_ctx__orelse.getText())
        #for i in range(return_children_number(ctx)):
        #    print(i,ctx.getChild(i).getText())
        #exit()
        #print(type(java_ctx__orelse))#.getText())
        # print("508", java_ctx__orelse.getText(), type(java_ctx__orelse))
        # 一文ずつ解析し、bodyに追加していく
        # ast_sen = return_sentence_tree(java_ctx__orelse)
        # ast_Java.Java8Parser.Java8Parser.StatementContext の型
        # print(java_ctx__orelse.getText())
        # exit()
        else:
            #print("577",ast_sen)
            ast_sen = make_tree_SC(java_ctx__orelse)
            print("511",ast_sen)
            ast_target.orelse.append(ast_sen)
            print("ここです２")
            print(ast_target.orelse)
            # 八百長：elseを全部からにする！
            # ast_target.orelse = []
            # listのためエラーになる
            # print(ast.dump(ast_target.orelse))
        
    print(ast.dump(ast_target))
    
    print(astunparse.unparse(ast_target))
    
    # exit()
    
    # 願望！！！！！！！！
    # うごけぇぇぇぇ！！
    # ast_target = Java2ast00.return_ast_conv_expr(word_list)
    # print(ast_target)
    # exit()
    
    return ast_target
    



# 再起的に木を作成します。(1語になったら子供がいなくなったらリストに追加する)
def make_word_list_Main(ctx):
    return_word_list = make_word_list(ctx, [])
    return return_word_list
    
def make_word_list(ctx, word_list):
    c_num = return_children_number(ctx)
    for i in range(c_num):
        child = ctx.getChild(i)
        if return_children_number(child) == 0:
            word_list.append(child.getText())
        else:
            make_word_list(child, word_list)
    return word_list
        


# argsの木から型と変数名を返却します。
def get_args(node_args):
    length = return_children_number(node_args)
    arg_type, arg_name = "", ""
    for i in range(length):
        txt = node_args.getChild(i).getText()
        if i + 1 == length:
            arg_name += txt
        else:  # 配列[]などの対応
            arg_type += txt
    return arg_type, arg_name


ans = []
ans1 = []
dic_t = dict()


def makeA(ctx, be=""):
    # print("be", be)
    p_txt = ctx.getText()
    num = return_children_number(ctx)
    for i in range(num):
        child = ctx.getChild(i)
        child_num = return_children_number(child)
        if child_num == 0:
            c_txt = child.getText()
            # print("親", ctx.getText())
            # print(i, txt)
            # print(ctx.getText(), "," , type(ctx))
            # 親をキーとする辞書
            dic_t.setdefault(p_txt, []).append(c_txt)
            ans.append(child.getText())
            ans1.append(child)
        else:
            makeA(child, p_txt)


# ここから動き始める
# プログラムの木構造を作る（メイン）
# listenerの木を変更していく
# やっぱり、listenerの木でなく、bodyを追加していった方が良き？listener.java_ast_body.append(＊＊＊)
def make_Tree(ctx, listener):
    # makeA(ctx)
    # print(ans)
    # print(ans1)
    # print(dic_t)
    # exit()
    # print("木構造の表示をします。")
    listener.root = Node("function", parent=None)
    # メソッドの木
    # print(type(ctx))
    # 子0：void
    # 子1：main
    # 子2：(String[] args)
    # 子3：プログラム
    # exit()
    num_children = return_children_number(ctx)
    print(ctx.getText())
    print("木の表示をする")
    # for i in range(num_children):
    #    print(i, ctx.getChild(i).getText())
    # exit()
    for i in range(num_children):
        child = ctx.getChild(i)
        # print("|" * 20, type(child))
        if i == 0 or i == 1:
            # そのままのテキスト
            # child_node = Node(child.getText(), parent=root)
            Node(child.getText(), parent=listener.root)
        elif i == 2:
            pass
            # voidあたりの宣言は無視する
            """# void main(String[] args)
            print(i, child.getText())
            #　引数のツリー
            child_node = Node("type_ast_args", parent=root)
            #   ├── args
            #   ├── (
            #   ├── Strings,inti
            #   └── )
            child = child.getChild(1)
            # ├── Strings
            # │   ├── ,
            # │   └── inti
            num = return_children_number(child)
            # 引数の数 = 子 ÷ 2 (切り上げ)
            # ⇒ カウンタが偶数の時
            for i in range(num):
                if i % 2 == 0:
                    # 複数の引数用 ＝ (型, 値)
                    # node_argの名前
                    # type_ast_arg
                    name_node_arg = "type_ast_arg" + str(i//2)
                    node_arg = Node(name_node_arg, parent=child_node)
                    args_child = child.getChild(i)
                    arg_type, arg_name = get_args(args_child)
                    # 型名と変数名をカウンタ葉に付ける
                    Node(arg_type, node_arg)
                    Node(arg_name, node_arg)
                    
                    show_NewTree(root)"""
                    
        elif i == 3:
            # bodyのつくり方
            # body_node = Node(child.getText(), parent=root)
            # このbody_Nodeに木を作る
            body_node = Node("body", parent=listener.root)
            # 現在のchild
            # <class 'ast_Java.Java8Parser.Java8Parser.MethodBodyContext>
            # 以下で更新する
            child = child.getChild(0)
            # 現在のchild
            # <class 'ast_Java.Java8Parser.Java8Parser.BlockContext'>
            # {
            # Scannersc=newScanner(System.in);inty=sc.nextInt();if(y%400==0)System.out.println("YES");elseif(y%100==0)System.out.println("NO");elseif(y%4==0)System.out.println("YES");
            # }
            #  以下で更新する
            # print(child.getText())
            body = child.getChild(1)
            # bodyの例
            # Scannersc=newScanner(System.in);inty=sc.nextInt();if(y%400==0)System.out.println("YES");elseif(y%100==0)System.out.println("NO");elseif(y%4==0)System.out.println("YES");
            # print(child.getText())
            # exit("751")
            body_num = return_children_number(body)
            # for i in range(body_num):
            #     print(i, body.getChild(i).getText())
            # exit("bodyの子供を表示した")
            # bodyにある文(ステートメント)を取得
            for i in range(body_num):
                # print(body.getChild(i).getText())
                # i番目の文を今から処理する
                now_body = body.getChild(i)
                # その文をテキストとして取得する
                line_txt = now_body.getText()
                # その分を木にする
                tree = return_sentence_tree(now_body, listener)
                # 木にした文の親(元文)を作成
                # body_all_node = Node(line_txt, parent=body_node)
                # 木を親にする
                # if tree is not None:
                #     tree.parent = body_all_node
                # 構文解析して単語一覧にしてみる？
                list_L = make_word_list_Main(now_body)
                print(list_L)
                print("treeの表示をする")
            

            # print()
            
            # show_NewTree(listener.root)
            # print("=" * 100)
            # {String s = "hello0"; (略) System.out.println("hello1");  
		    # {String s = "hello0"; (略) System.out.println("hello1");  <class 'ast_Java.Java8Parser.Java8Parser.BlockContext>
            # type_ast_BlockContext
            # 子どもの更新
            # <class 'ast_Java.Java8Parser.Java8Parser.BlockContext>
            child = child.getChild(0)
            node_ast_block = Node("type_ast_BlockContext", parent=listener.root)
            # ブロックの中のこの数
            num_inBlock = return_children_number(child)
            for i in range(num_inBlock):
                # print(child.getChild(i).getText())
                # 1文ずつ解析結果を木にする (ブロックの場合)
                child_block = child.getChild(i)  # 2種類のどちらか？
                # >>>>>>>>>> <class 'antlr4.tree.Tree.TerminalNodeImpl'>
                # >>>>>>>>>> <class 'ast_Java.Java8Parser.Java8Parser.BlockStatementContext'>
                # print("_" * 100)
                print("type(child_block)", type(child_block))
                print(child_block.getText())
                print(type(child_block) ==
                      ast_Java.Java8Parser.Java8Parser.BlockStatementsContext)
                print(return_children_number(child_block))
                if type(child_block) == ast_Java.Java8Parser.Java8Parser.BlockStatementsContext:
                    for child_block2 in child_block.getChildren():
                            
                        # ast_Java.Java8Parser.Java8Parser.BlockStatementContext
                        # ⇒ >>>>>>>>>> <class 'ast_Java.Java8Parser.Java8Parser.StatementContextなどで
                        tree_sentence=return_sentence_tree(child_block2, listener)
                        print(child_block2.getText())
                        print(type(child_block2))
                        # 文の親をブロックに設定
                        return_tree=add_parent(tree_sentence, node_ast_block)
                    # exit()
                else:  # 括弧の時
                    pass
            # print("=" * 100)

        else:
            # エラー出力
            print('予期しない子どもがあります。', file = sys.stderr)
            sys.exit(1)

        print(listener.root)
        print(child.getText())
        print(return_children_number(child.getChild(0)))
    # exit()
    # メソッド構文木の返却
    print("返却します")
    return listener.root

    """
    ctx_p = ctx.parentCtx
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
    """
