class yao():
    def __init__(self):
        # 方法の番号
        # 0. insert 1. delete   2. replace
        self.yao_way_num = 1
        # 修正前に対しての削除するブロック
        self.yao_delete_num = 11
        # 外部ソースコードの選択。
        # 例：(n個の外部ソースコード：0 以上、n-1以下)
        self.yao_sel_num = None
        # 修正に利用する外部ソースコードのブロック
        self.yao_ext_num = None
        # 挿入の場合の挿入する親ブロック(挿入以外はNoneでOK)
        self.insert_id = None
        
        # 八百長なし
        self.yao_way_num = None
        self.yao_delete_num = None
        self.yao_sel_num = None
        self.yao_ext_num = None
        self.insert_id = None

        
    def update_way_num(self, way_num):
        if self.yao_way_num is not None:
            return self.yao_way_num
        else:
            return way_num
        
    def update_delete_num(self, delete_num):
        if self.yao_delete_num is not None:
            return self.yao_delete_num
        else:
            return delete_num
        
    def update_sel_num(self, sel_num):
        if self.yao_sel_num is not None:
            return self.yao_sel_num
        else:
            return sel_num
    
    def update_ext_num(self, ext_num):
        if self.yao_ext_num is not None:
            return self.yao_ext_num
        else:
            return ext_num
        
    def update_insert_id(self, insert_id):
        if self.insert_id is not None:
            return self.insert_id
        else:
            return insert_id