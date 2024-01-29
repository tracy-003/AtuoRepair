# 親をみてコードを出力する
import ast
import astunparse

class ast2py:
    def __init__(self,mB):
        self.mB = mB
        self.logger = mB.logger

    def make_code(self, parend_id):
        #for i in range(self.mB.cnt+1):
        #    print(str(i) + ": " + str(self.mB.dic_stats[i]))
            
        # print("parent_id: " + str(parend_id))
        # print(self.mB.dic_children)
        # print(self.mB.sIds)
        # print("parend_id: " + str(parend_id))
        
        # print(self.sIds[parend_id])
        
        code1 = "\t" * (self.mB.sIds[parend_id] - 1)
        # 前後の改行をなくした文
        # ブロックをidから取得する
        ast_list = self.mB.dic_stats[parend_id]
        code2 = ""
        for ast_code in ast_list:
            # ast_codeがastオブジェクトの場合
            if ast.AST in (type(ast_code).__mro__):
                code2 += str(astunparse.unparse(ast_code)).strip("\n")
            else: # それ以外の場合は、str型？になっているはず！
                code2 += str(ast_code)
        # print(i-1, tabs_num[i]-1)
        code = code1 + code2 + "\n"
        # 子がある場合さらに深く調べる
        if parend_id in self.mB.dic_tree:
            # code += self.make_code(self.dic_tree[parend_id])
            # insert_id=0かつext_id=0の時に発生
            try:
                code = self.return_code(parend_id, code)
            except Exception as e:
                self.logger.error("RecursionError")
                self.logger.error(e)
                exit(1)
        #self.logger.info(str(code))
        return code

    def return_code(self, now_id = 0, code = ""):
        # 子どもを持っていないときは0を変換して返却
        if now_id not in self.mB.dic_tree:
            # print(list_codes)
            code = self.make_code(0)
            
        else:
            children = self.mB.dic_tree[now_id]
            for child_id in children:
                # print(str(child_id) + "の変換を開始します。")
                code += self.make_code(child_id)
        
        return code