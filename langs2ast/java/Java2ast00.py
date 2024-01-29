# pythonのastモジュールを作成するプログラム
import ast
# import astunparse

from langs2ast.java import Java_Checker

def make_ast(body):
    # node = ast.UnaryOp(ast.USub(), ast.Constant(value=5))
    mod = ast.Module()
    mod.body = body
    mod.type_ignores = []
    # ここから本体部分
    # mod.body.append(return_Assign("a", 8))
    # mod.body.append(return_If())
    return mod

def return_input():
    # input関数の返却をします。
    object_ast = ast.Call(func=ast.Name(id='input', ctx=ast.Load()))
    return object_ast

def return_return(return_val = None):
    # returnのみの関数
    object_ast = ast.Return()
    object_ast.value = return_val
    return object_ast

def return_input_int():
    object_ast = ast.Call()
    object_ast.func = ast.Name(id='int', ctx=ast.Load())
    call_obj = return_input()
    call_obj.args = []
    call_obj.keywords = []
    object_ast.args = [call_obj]
    object_ast.keywords = []
    return object_ast

def return_AugAssign(name, op, id):
    # AugAssignするときは、初期値というか、そういうのはあるでしょ？
    # == idの型の親にastがある
    object_ast = ast.AugAssign()
    # 変数名は、値がastだろうが他のだろうが一緒！！
    object_ast.target = [ast.Name(id = name, ctx = ast.Store())]
    # 演算子も同様！！
    # +=じゃなくて「+」で検索しようぜ！
    #print(return_objY(op[0]))
    #exit()
    ast_op = return_objY(op[0])[0]
    print("=" * 5 , "警告", "=" * 5 , "演算子がおかしいかもしれません！！")
    object_ast.op = ast_op

    if ast.AST in (type(id).__mro__):
        print("Java2ast00.py: return_Assign: id is ast")
        object_ast.value = id
        # exit(object_ast)
        return object_ast
    
    else:
        # (str型のみ) idに引用符がついてる時は取り除く
        if type(id) == str:
            id = id.replace('"', '')
        # print("代入する値", id)
        
        # 値が標準入力のときは、Trueと型のタプルを返却します。
        isInput_L = Java_Checker.check(str(id))
        if isInput_L[0]:
            # 肩を判断せずにint型の標準入力として代入します。
            object_ast.value = return_input_int()
        # 普通の値の時。
        else:
            object_ast.value = ast.Constant(value=id, kind = None)
        return object_ast



def return_Assign(name, id):
    # 代入するastツリーを返却します。
    # 引数 → name:変数名, id:値 
    # idがもうastオブジェクトの時
    # == idの型の親にastがある
    if ast.AST in (type(id).__mro__):
        print("Java2ast00.py: return_Assign: id is ast")
        object_ast = ast.Assign()
        object_ast.targets = [ast.Name(id = name, ctx = ast.Store())]
        object_ast.value = id
        # exit(object_ast)
        return object_ast
    
    else:
        # (str型のみ) idに引用符がついてる時は取り除く
        if type(id) == str:
            id = id.replace('"', '')
        # print("代入する値", id)
        object_ast = ast.Assign()
        object_ast.targets = [ast.Name(id = name, ctx = ast.Store())]
        # 値が標準入力のときは、Trueと型のタプルを返却します。
        isInput_L = Java_Checker.check(str(id))
        if isInput_L[0]:
            # 肩を判断せずにint型の標準入力として代入します。
            object_ast.value = return_input_int()
        # 普通の値の時。
        else:
            object_ast.value = ast.Constant(value=id, kind = None)
        return object_ast

def return_Assign_input(name):
    # 標準入力から代入するastツリーを返却します。
    # 引数 → name:変数名 右辺はかならずinput()
    object_ast = ast.Assign()
    object_ast.targets = [ast.Name(id = name, ctx = ast.Store())]
    object_ast.value = return_input()
    
    return object_ast

def return_print_Call(name):
    if type(name) == str:
        name = name.replace('"', '')
    obj_ast_call = ast.Call(func=ast.Name(id='print', ctx=ast.Load())
                            , args=[ast.Constant(value=name, kind=None)])
    return obj_ast_call

def return_print(name, isN = False):
    # 改行の有無：isN
    object_ast = ast.Expr()
    object_ast.value = return_print_Call(name.getText())
    # print(ast.dump(ast.parse("print('a')")))
    # Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='a', kind=None)], keywords=[]))], type_ignores=[])
    # print(ast.dump(ast.parse("print('a',end='')")))
    # Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='a', kind=None)], keywords=[keyword(arg='end', value=Constant(value='', kind=None))]))], type_ignores=[])
    if isN:
        # object_ast.value.keywords.arg = 'end'
        # object_ast.value.keywords.value = ast.Constant(value='', kind=None)
        object_ast.value.keywords = [ast.keyword(arg='end', value=ast.Constant(value='', kind=None))]
    else:
        object_ast.value.keywords = []

    # print(astunparse.unparse(object_ast))
    # print(ast.dump(object_ast))
    
    return object_ast
    
"""def return_If():
    name = "test"
    ast_enzan = ast.Gt()
    val = 3
    # if文を返却します。
    object_ast = ast.If()
    object_ast.test = ast.Compare(
        ast.Name(id = name, ctx = ast.Load())
        , [ast_enzan]
        , [ast.Constant(value=val, kind = None)]
    )
    object_ast.body = [
        ast.Pass()
    ]
    object_ast.orelse = [
        ast.Pass()
    ]
    return object_ast"""
    
def return_symbol(s):
    if s == "==":
        return [ast.Eq()]
    elif s == "<=":
        return [ast.GtE()]

def main(body):
    print("Java2ast00.py: main: start 120",body)
    ast_object = make_ast(body)
    
    # print(astunparse.unparse(ast_object))
    return ast_object
    
if __name__ == '__main__':
    main()
    
    

#===============================================================================
# 単語からastオブジェクトと優先度を返却する
def return_objY(word):
    # 演算子系？
    if word == "*":
        return (ast.Mult(),41-4)
    if word == "/":
        return (ast.Div(),41-4)
    if word == "%":
        return (ast.Mod(),41-4)
    if word == "+":
        return (ast.Add(),41-5)
    if word == "-":
        return (ast.Sub(),41-5)
    if word == "<<":
        return (ast.LShift(),41-6)
    if word == ">>":
        return (ast.RShift(),41-6)        
    if word == ">":
        return (ast.Gt(),41-7)
    if word == ">=":
        return (ast.GtE(),41-7)        
    if word == "<":
        return (ast.Lt(),41-7)
    if word == "<=":
        return (ast.LtE(),41-7)
    if word == "==":
        return (ast.Eq(),41-8)
    if word == "!=":
        return (ast.NotEq(),41-8)
    if word == "&":
        return (ast.BitAnd(),41-9)
    if word == "^":
        return (ast.BitXor(),41-10)
    if word == "|":
        return (ast.BitOr(),41-11)
    if word == "&&":
        return  (ast.BoolOp(ast.And()),41-12)
    if word == "||":
        return (ast.BoolOp(ast.Or()),41-13)
    if word == "(":
        return ("(",40)
    if word == ")":
        return (")",41)
    
    
    
    else:
        print("未知のトークンです。", word)
        # 数字にできるときは、定数にする
        if word.isdigit():
            return (ast.Constant(value=int(word), kind=None),0)
        # trueやfalseの時もelseでok
        # 数字にできないときは、変数にする
        else:
            return (ast.Name(id=word, ctx=ast.Load()),0)
        