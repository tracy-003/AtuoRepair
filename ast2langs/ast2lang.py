# ASTからコードに変更する
"""class exchange_Block:
    def __init__(self, mB):
        self.mB = mB"""

from ast2langs import ast2python
from ast2langs import ast2java
# どんな言語でもASTから変換する
def return_All_code(mB, now_id=0, code=""):
    # 言語をしらべて、コードを返す
    # テキスト型でok!
    lang = mB.language_type
    print("言語は", lang, "です")
    
    if lang == "python":
        obj_ast2py = ast2python.ast2py(mB)
        code = obj_ast2py.return_code(now_id, code)
        
        # print("修正後コードの出力です。")
        # print("*" * 50)
        # print(code)
        # print("*" * 50)
        # exit("exit:ここで終了します。")
        
        code = check_code(code, mB)
        
        return code
    
    elif lang == "java":
        
        obj_ast2py = ast2python.ast2py(mB)
        code = obj_ast2py.return_code(now_id, code)
        print("*" * 35, "ast2lang.py:34" ,"*" * 35)
        print(code)
        print("*" * 100)
        code = check_code(code, mB)
        # コードが正しくないときは、Noneを返す
        print(code)
        if code == None:
            return None
        
        
        # print(code)
        # all_ast = ast.parse(code)
        obj_ast2java = ast2java.ast2java(code)
        
        java_code = obj_ast2java.main()
        # print(java_code)
        """# print(all_ast)
        p0 = mB.dic_stats[0]
        import astunparse
        print(astunparse.unparse(p0))
        
        print("-" * 30)
        
        max_num = len(mB.dic_stats) - 1
        for i in range(max_num):
            li = mB.dic_stats[i]
            # print("li", li)
            for s in li:
                # print(s)
                if type(s) is str or type(s) is int:
                    pass
                else:
                    print(astunparse.unparse(s))
        """
        # exit(java_code)
        return java_code
        
    else:
        exit("ast2lang.py: return_All_code: 未対応の言語です。")



def check_code(rep_code, mB):
    # ブロックはパスを知るためだけに使用する。
    input_path = mB.input_path
    # write rep_code to file
    file = open(r"_output.py", "w")
    # file.writelines("#" + str(input_path))
    # file.writelines("\n")
    file.writelines(rep_code)
    file.close()
    
    
    # ⅹ 世代数はカウントしない
    # 正しくないときは、Noneを返す
    try:
        compile(rep_code, '', 'exec')
    except Exception as e:
        print("修正後のコード：" + str(e))
        return None
    return rep_code
    


#def main(): 
#    input_Path = r"C:\Users\user\new_study\trans\make_middle\PY01\AC001.py"
#    
#    import make_Block
#    
#    # ロガーの設定
#    import json
#    from logging import getLogger, config
#    # ログファイルの取得
#    with open('log_config.json', 'r') as f:
##        log_conf = json.load(f)
#    config.dictConfig(log_conf)
#    logger = getLogger(__name__)
#    
#    mB = make_Block.main(logger, input_Path)
#    return return_All_code(mB)
#if __name__ == "__main__":
#    main()

