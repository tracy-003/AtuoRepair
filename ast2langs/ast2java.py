import ast

from ast2langs import type2java # pythonの型クラスからjavaの型クラス(文字列)に変換する関数
import ast_indent
# 整数かどうかを調べる関数
def is_int(num):
    if num.isnumeric():
        return True
    else:
        return False
    """#　負の数に対応するため
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True
"""
    # s = "12"
    # s = "-3"
    # s = "3.0"
    # s = "-3.0"


# 小数かどうかを調べる関数
def is_float(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True

# 変更する関数


class ast2java:
    # codeはpythonで可
    def __init__(self, code):
        # コードを引数として与える
        self.code = code
        # 引数のコードからbodyをリストにする
        self.ast_list = ast.parse(code).body
        # codeに含まれている変数名と型(クラス)を辞書にする
        self.dic_name = dict()
        # 変数名の集合
        self.names = set()
        # javaの特別な識別子：true,false
        self.names_boolean = {"true","false"}



    # 文字列sから型(クラス)を返却するプログラム
    def return_type_class(self, s):
        # print("type(s) is ast.UnaryOp", type(s) is ast.UnaryOp)
        # 負の数
        # <_ast.UnaryOp object at 0x000001F1EE83D400>
        # UnaryOp(op=USub(), operand=Constant(value=3, kind=None)), type_comment=None)
        if type(s) is ast.UnaryOp:
            val = self.ast_expr(s.operand)
            # マイナス以外を取り出して再判断する
            return self.return_type_class(val)
        # 文字列のとき
        if type(s) == str:
            # 整数型
            if isinstance(s, int):
                return type(0)
            # 整数値
            elif is_int(s):
                return type(0)
            # 小数値
            elif is_float(s):
                # print(s ,"は小数値です")
                return type(0.0)
            # 他は変数名、文字列
            else:
                # 辞書内になかったら文字列
                if s not in self.dic_name:
                    return type("")
                # 辞書にあったら文字列変数名
                else:
                    return self.dic_name[s]
        # 文字列以外のとき
        else:
            return type(s)
        
    def ast_cmpop(self, object):
        object_type = type(object)
        if object_type == ast.Eq:
            return "=="
        elif object_type == ast.NotEq:
            return "!="
        elif object_type == ast.Lt:
            return "<"
        elif object_type == ast.LtE:
            return "<="
        elif object_type == ast.Gt:
            return ">"
        elif object_type == ast.GtE:
            return ">="
        else:
            return "ast_cmpop: 未対応のオブジェクトです。" + str(object_type)
        
    def ast_operator(self, object):
        object_type = type(object)
        if object_type == ast.Add:
            return "+"
        elif object_type == ast.Sub:
            return "-"
        elif object_type == ast.Mult:
            return "*"
        elif object_type == ast.Div:
            return "/"
        elif object_type == ast.Mod:
            return "%"
        # elif object_type == ast.Pow:
        #     return "**"
        else:
            return "ast_operator: 未対応のオブジェクトです。" + str(object_type)

    def ast_boolop(self, object):
        object_type = type(object)
        if object_type == ast.And:
            return "&&"

        elif object_type == ast.Or:
            return "||"

    def ast_expr(self, object):
        object_type = type(object)
        if object_type == ast.Name:
            # Name(identifier id, expr_context ctx)
            # ほとんどが変数名
            return object.id

        elif object_type == ast.Constant:
            return object.value
        
        elif object_type == ast.Compare:
            # Compare(expr left, cmpop* ops, expr* comparators)
            compare_lef = str(self.ast_expr(object.left))
            compare_cmp = str(self.ast_cmpop(object.ops[0]))
            compare_com = str(self.ast_expr(object.comparators[0]))
            # print(compare_lef, compare_cmp, compare_com)
            return compare_lef + compare_cmp + compare_com
            
        elif object_type == ast.BinOp:
            # BinOp(expr left, operator op, expr right)
            bin_lef = str(self.ast_expr(object.left))
            bin_opr = str(self.ast_operator(object.op))
            bin_rig = str(self.ast_expr(object.right))
            # print(bin_lef, bin_opr, bin_rig)
            # exit()
            return bin_lef + bin_opr + bin_rig

        elif object_type == ast.Call:
            # print(ast.dump(object))
            txt_call = ""
            # 出力printの時
            if type(object.func) == ast.Name:
                if object.func.id == "print":
                    txt_call = "System.out.println("
                    for arg in object.args:
                        val = self.ast_expr(arg)
                        s = ""
                        
                        # 変数名の名前が含まれている場合は、そのまま
                        if val in self.names:
                            pass

                        elif type(val) == type(""):
                            s = '"'
                        
                        
                        txt_call += s
                        txt_call += val
                        txt_call += s
                        
                    txt_call += ");\n"
                else:
                    print("ast_expr(AST.func.id): 未対応のオブジェクトです。" + str(object_type))
            else:
                print("ast_expr(AST.Call): 未対応のオブジェクトです。" + str(object_type))
            return txt_call
        
        elif object_type == ast.BoolOp:
            print("ast.java：175：論理演算をします。")
            # とりあえず、論理演算は2つで考える！！
            import astunparse
            print(astunparse.unparse(object))
            ast_log_syn = object.op
            ast_log_vals = object.values
            # print(self.ast_expr(ast_log_vals[0]))
            
            val1 = self.ast_expr(ast_log_vals[0])
            op_L = self.ast_boolop(ast_log_syn)
            val2 = self.ast_expr(ast_log_vals[1])

            print(val1,op_L,val2)
            print("論理演算終了")

            return val1 + op_L + val2

            # print(ast.dump(object))
        else:
            print("ast_expr : object_type == ast.BoolOp → ",object_type == ast.BoolOp)
            exit("ast_expr: 未対応のオブジェクトです。" + str(object_type))
        

    def ast_stmt(self, object):
        object_type = type(object)
        if object_type == ast.Assign:
            # Assign(expr* targets, expr value, string? type_comment)
            print("AssignのAST ========================================")
            print(ast.dump(object))
            tar = self.ast_expr(object.targets[0])
            # valはコンスタント型orUnaryOp型（マイナスの時）
            val = object.value
            # Constant型のvalue(値)を取得
            if type(val) == ast.Constant:
                val = val.value
            # 負の数の時
            elif type(val) == ast.UnaryOp:
                # UnaryOpクラスのop = Usub()のとき
                val = self.ast_expr(val.operand) * -1
                # print("103", val)
            """
            else:
                print(ast.dump(val))
            """
            # print(val)
            val_type = self.return_type_class(val)

            java_type = type2java.ex(val_type)
            print("-" * 30, "代入をします")
            print("変数名", tar , "は", end = "")
            # 既出の変数名の場合
            if tar in self.names:
                print("既出です。",end = "代入する値：")
                print(val, end =" の型は、")
                # 入れる値が標準入力の場合
                print(type(val))
                print("type(val) == ast.Call" , type(val) == ast.Call,)
                if type(val) is ast.Call:
                    # print(ast.dump(val))
                    # Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='input', ctx=Load()), args=[], keywords=[])], keywords=[])
                    if type(val.func) is ast.Name:
                        if val.func.id == 'int':
                            if type(val.args[0]) is ast.Call:
                                if type(val.args[0].func) is ast.Name:
                                    if val.args[0].func.id == 'input':
                                        code_R = "Scanner sc = new Scanner(System.in);\n"
                                        code_R += str(tar) # 変数名
                                        code_R += " = "
                                        code_R += "sc.nextInt();\n"
                                        return code_R
                                    else:
                                        exit("ast2java.pyで例外が起こっています：248") 
                                else:
                                    exit("ast2java.pyで例外が起こっています：250") 

                            else:
                                exit("ast2java.pyで例外が起こっています：253") 

                        else:
                            exit("ast2java.pyで例外が起こっています：256") 

                    else:
                        exit("ast2java.pyで例外が起こっています：") 

                else:
                    si = ""
                    if java_type is "String":
                        si = '"'
                    else:
                        pass # intの時、boolの時

                    code_R = str(tar)
                    code_R += " "
                    code_R += "="
                    code_R += " "
                    code_R += si
                    code_R += str(val)
                    code_R += si
                    # code_R += " "
                    code_R += ";\n"
                    return code_R


            # 初めての変数名
            else:
                print("初です", "ast2java.py")
                print("その方は、", java_type, val_type, val, tar)
                if java_type is None:
                    print("おそらく、標準入力です。int型にしてあります")
                    code_R = ""
                    code_R += "Scanner sc = new Scanner(System.in);\n"
                    code_R += "int " # 型名
                    code_R += str(tar) # 変数名
                    code_R += " = "
                    code_R += "sc.nextInt();\n"
                    # print("code_R",code_R)
                    return code_R
                
                else:
                    # 変数名の辞書に、初めての変数名を追加する。
                    self.names.add(tar)
                    # 多分標準入力？
                    if java_type is None:
                        # おそらく標準入力
                        code_R = ""
                        code_R += "Scanner sc = new Scanner(System.in);\n"
                        code_R += "int " # 型名
                        code_R += str(tar) # 変数名
                        code_R += " = "
                        code_R += "sc.nextInt();\n"
                        # print("code_R",code_R)
                        print("代入のコード：\n", code_R)
                        print("$" * 30)
                        return code_R
                    
                    # boolean型の時
                    elif val in self.names_boolean:
                        code_R = "boolean"
                        code_R += " "
                        code_R += str(tar)
                        code_R += " "
                        code_R += "="
                        code_R += " "
                        code_R += str(val).lower() # javaの場合は、小文字で宣言する
                        # code_R += " "
                        code_R += ";\n"

                    else:
                        si = ""
                        if java_type is "String":
                            si = '"'

                        code_R = str(java_type)
                        code_R += " "
                        code_R += str(tar)
                        code_R += " "
                        code_R += "="
                        code_R += " "
                        code_R += si
                        code_R += str(val)
                        code_R += si
                        # code_R += " "
                        code_R += ";\n"
                        # print("code_R",code_R)
                        print("再代入のコード：", code_R)
                        return code_R

        elif object_type == ast.If:
            # If(
            # test=Compare(left=BinOp(left=Name(id='i', ctx=Load()), op=Mod(), right=Constant(value=4, kind=None)), ops=[Eq()], comparators=[Constant(value=0, kind=None)])
            # , body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='Yes', kind=None)], keywords=[]))]
            # , orelse=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='No', kind=None)], keywords=[]))]
            # )
            # if文の典型
            if_st = ""
            if_st += "if("
            if_st += str(self.ast_expr(object.test))
            if_st += "){\n"
            # 真のときのブロック
            for obj in object.body:
                sent = str(self.ast_stmt(obj))
                if sent != "":
                    if_st += sent
            if_st += "}\n"
            if_st += "else{\n"
            for obj in object.orelse:
                sent = str(self.ast_stmt(obj))
                if sent != "":
                    if_st += sent
            # print(ast.dump(object))
            if_st += "}\n"
            return if_st
        
        elif object_type == ast.Expr:
            # Expr(expr value)
            return self.ast_expr(object.value)

        elif object_type == ast.While:
            txt_while = "while("
            txt_while += self.ast_expr(object.test)
            txt_while += "){\n"
            list_block = object.body
            for sen in list_block:
                txt_while += self.ast_stmt(sen)
            txt_while += "}\n"
            # print(txt_while)
            return txt_while

        else:
            exit("ast_stmt: 未対応のオブジェクトです。" + str(object_type))



    def main(self):
        # print(ast.dump(ast_object))
        # import文を追加
        return_code = "import java.util.Scanner;\n"
        # javaの典型
        return_code += "public class _output2 {\n"
        return_code += "public static void main(String[] args) {\n"
        # javaのボディー
        # print(ast_list)
        ast_list=self.ast_list
        for ast_object in ast_list:
            # 変換後
            ex_ast = self.ast_stmt(ast_object)
            print("ast_objectの表示：",ast_object , ">>",ex_ast )
            if ex_ast is not None:
                return_code += ex_ast
            else:
                from logging import getLogger
                logger = getLogger(__name__)
                logger.error("ast_stmtがNoneです")

            print(return_code)

        # javaの終わり
        return_code += "}\n}"
        return return_code

# テスト動作用
if __name__ == '__main__':
    FILENAME=r"C:\Users\user\new_study\trans\make_middle\testPy03.py"
    # pythonのプログラム
    code=""
    try:
        # 文字コード指定なし
        # with open(FILENAME, 'r', encoding="UTF-8"):
        with open(FILENAME, 'r') as f:
            code=f.read()

    except Exception as e:
        # エラー例
        # パスが「\」→ 「\\」
        print(str(e))
        exit(1)

    # ast_モジュールで構文解析
    # ast_list_code = ast.parse(code).body
    ast_obj=ast.parse(code)
    # グローバル変数の初期化(複数ファイル変換しないので不要)
    """# パラメータの設定
    input_file = "python_urus\\bpy001.py"
    # 出力ファイル名は決まっているので、パスを指定してください。
    # デフォルトでは、このファイルと同じディレクトリに出力されます。
    # 例：out_path = "out/new_all/"
    out_path = "out/"
    """
    print(str(FILENAME) + " の変換を始めます。")
    # s = time.perf_counter()
    # 中間言語を表示
    # write into file
    # print()

    file=open(r"C:\Users\user\new_study\trans\make_middle\middle_ast.txt", "w")
    s = ast_indent.show(ast.dump(ast_obj))
    file.writelines(s)
    file.close()
    # ast2javaクラスの作成
    obj_ast2java=ast2java(ast_obj)
    # mainで変換する
    txt=obj_ast2java.main()
    #print("#" * 30)
    #print(txt)
    # import pprint
    # pprint.pprint(txt, indent = 4)
    # e = time.perf_counter()
    file=open(r"C:\Users\user\new_study\trans\make_middle\out_java.java", "w")
    file.writelines(txt)
    file.close()
    print(str(FILENAME) + " の変換が終わりました。")
    