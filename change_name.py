# https://qiita.com/t2y/items/c8877cf5d3d22cdcf2a8
import ast

class Transformer(ast.NodeTransformer):
    def __init__(self,
                 ast_ext,
                 mB_source,
                 mB_ext):
        # 修正するast
        self.ast_ext = ast_ext
        # 元のソースコード(ブロック)・型辞書
        self.mB_source = mB_source
        # self.diciden_source = mB_source.dic_identifier
        # 外部のソースコード(ブロック)・型辞書
        self.mB_ext = mB_ext
        # 外部ソースコードの変数名リスト
        self.ext_names = self.make_names(mB_ext)
        # self.diciden_ext = mB_ext.dic_identifier
        # 挿入する部分の外部id
        # self.ext_num = ext_num
        # その外部idを使って取得した、挿入する部分のastなど
        # self.list_ext_code = mB_ext.dic_stats[ext_num]
        
        
    def make_names(self, block):
        """dic = block.dic_type2name
        vals = list(dic.values())
        length = len(vals)

        names = [""] * length
        for i in range(length):
            # 同じ型の[変数名,id] * n 二次元配列 
            type_array = vals[0]
            array = type_array[0]
            names[i] = array[0]
            
        print("names:", list(block.dic_name2type.keys()))
        """
        # 変数名→型のキーのみを取り出す
        return list(block.dic_name2type.keys())
        
        
    def visit_Name(self, node):
        # その名前がもしも外部の変数名だったら
        if node.id in self.ext_names:
            # 外部の型辞書からその名前の型を知る
            # 変数名 → 型
            # ここがおそらくミス
            # 外部のブロックから型を取得する
            type_name = self.mB_ext.dic_name2type[node.id]
            # print(type_name)
            # その型の変数名を元のソースコードから候補を探す
            # 型 → 変数名
            
            try:
                list_name_cand = self.mB_source.dic_type2name[type_name]    
                # 候補の中からランダムに1つを選ぶ
                import random
                # 置き換える変数名とスコープidのペア
                re_pair = random.choice(list_name_cand)
                re_name = re_pair[0]
                
            except KeyError:
                print("型が見つかりませんでした。")
                re_name = "none"

            # 変更するためのNameノードを作成
            name_node = ast.Name(id=re_name, ctx=ast.Load())
            # このノードを置き換える
            return ast.copy_location(name_node, node)
        else:
            return node

# 変数名を変更したASTを出力    
def change_name(ast_ext,mB_source,mB_ext,ext_num):
    #print(astunparse.unparse(tree))
    trans_ast = Transformer(
        ast_ext,
        mB_source,
        mB_ext,
    )
    # print(ast_ext)
    # <_ast.BoolOp object at 0x000001FB474132B0>
    ast_code = trans_ast.visit(ast_ext)
    # print("=" * 20)
    # print(astunparse.unparse(ast_code))
    # print("=" * 20)
    return ast_code
    
if __name__ == '__main__':

    f = open('vis01.py', 'r')
    list_code = f.readlines()
    source = ""
    for txt in list_code:
        source += txt

    # コードをASTに変換
    tree = ast.parse(source)
    
    change_name(tree)