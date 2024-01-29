import yaotyou_setting # 実動作には不要なコード

import change_name  # ASTを解析して変数名を対応させてくれるモジュール

from ast2langs import ast2lang

class Repair_Block:
    def __init__(self, logger, make_Block, mB_exts):
        self.logger = logger
        self.mB_source = make_Block
        self.mB_exts = mB_exts
        # 置換するときに使用。
        # 置換：削除 → 挿入　削除時のidを取得
        self.temp_id = None
        # 削除しようとした回数
        self.try_delA = 0
        # ======統計用=========
        self.way = None        # 使った修正方法
        self.del_num = None    # 削除したId
        self.insert_parent = None  # 挿入する親のId
        self.insert_id = None  # 挿入するId(文章)
        self.ext_id = None     # 外部ソースコードのId(0から始まる)を引数に、
        
        # ============================
        # ~~~  実動作には不要  ~~~
        self.yao = yaotyou_setting.yao()
        # ============================

    def getRandom_insert_num(self, block):
        # 親になることのできる集合から選択
        import random
        list_parentalble = list(block.set_parentable)
        length = len(list_parentalble)
        num = random.randint(0, length - 1)
        
        print("25:getRandom_insert_num: " +
              str(list_parentalble) + "から選択してます >>", num)
        return list_parentalble[num]

    # この関数は、引数の集合のうち、ランダムに選択する
    def getRandom_from_set(self, set_arg):
        import random
        list_arg = list(set_arg)
        length = len(list_arg)
        num = random.randint(0, length - 1)
        return list_arg[num]

    # 外部ソースコードのidをランダムに選択する
    def getRandom_source_num(self, argv, isMoju=False):
        import random
        # get random number
        # 0はモジュール全体なので、1から始める
        # モジュール全体が必要な時は、isMojuをTrueにする
        start_num = 1
        if isMoju:
            start_num = 0
        self.logger.info("始まりは、" + str(start_num) + "　終わりは、" + str(argv-1) + "です")
        num = random.randint(start_num, argv - 1)

        return num

    # 削除を行う関数
    def delete_block(self, isRep=False, isM=False):
        # 削除するモニター：何回も削除しようとしてエラーになるのを防ぐ
        # self.try_delA に値を入れる
        # それを親とするノード以下は削除：親を見つけて、その親から自身を削除する
        # ランダムで選択
        # ステートメント系じゃなくて、一文削除もするのでここはsource_num
        # print(self.mB_source.set_all)
        # print(self.mB_source.set_decl)
        # 宣言文以外の削除
        set_withoutDecl = self.mB_source.set_all - self.mB_source.set_decl
        print("set_withoutDecl", set_withoutDecl)
        delete_num = self.getRandom_from_set(set_withoutDecl)
        # 八百長
        delete_num = self.yao.update_delete_num(delete_num)

        # 統計用
        self.del_num = delete_num
        # print(delete_num, isRep)
        if delete_num == 0:
            """
            if isRep:
                # 置換する場合は全部削除する
                self.logger.info("モジュール全体を削除")
                self.mB_source.delete_module()
                # とりあえず削除した場所を記憶する
                self.temp_id = 0
                # 削除したら別メソッドで挿入する
                return
            else:
                self.try_delA += 1
                # 置換しないのにモジュール全体を削除するのはおかしい
                self.logger.warning("モジュール全体を削除しようとした")
                self.logger.warning(str(delete_num) + " " + str(isRep))
                # 挑戦回数が2回以下だったらもう一度削除する
                if self.try_delA <= 2:
                    self.delete_block()
                # 違ったら全体を終わらしたい
                else:
                    self.logger.warning("何回もモジュール全体を削除しようとした")
                    return
            """
            return

        else:
            self.logger.info(delete_num)
            self.logger.info(self.mB_source.dic_stats)
            self.logger.info(self.mB_source.dic_children)

            # とりあえず削除した場所を記憶する
            # 置換用の記録なので、ここで親を記録する
            # self.logger.info("削除するId:" + str(delete_num))
            if delete_num == 0:
                self.temp_id = 0
            #elif delete_num not in self.mB_source.dic_children:
            #    pass
            else:
                self.temp_id = self.mB_source.dic_children[delete_num]

            # self.logger.info("削除する親のId:" + str(self.temp_id))
            # 統計用
            self.del_num = delete_num
            # 何も削除する
            # print("84",self.mB_source.dic_children)
            # self.mB_source.dic_children[delete_num] = None
            # 親を取得する
            # parent_id = None
            # 親がいないときは、Noneが返ってくる
            # if parent_id in self.mB_source.dic_children:
                
            # parent_id = self.mB_source.dic_children[delete_num]
            print("delete_num", delete_num, self.mB_source.dic_children)
            parent_id = self.mB_source.dic_children[delete_num]
            # delete_numが含まれている同じレベルのリストを取得
            self.logger.info("仲間探し: " + str(parent_id) + " " +
                            str(self.mB_source.dic_children))
            self.logger.info("ここから探します。" + str(set_withoutDecl))
            children_list = self.mB_source.dic_tree[parent_id]
            self.logger.info("children_list: " + str(children_list))
            # delete_numを削除
            children_list.remove(delete_num)
            # children_listを更新
            self.mB_source.dic_tree[parent_id] = children_list
            self.logger.info("children_list: " + str(children_list))
            # self.logger.info(str(self.mB_exts[0].return_code()))
            # self.logger.info(str(self.mB_exts[1].return_code()))

            #削除するのは一番最後に！！
            self.mB_source.dic_children[delete_num] = None

        self.logger.info("削除を行った" + str(self.temp_id))

    # """#　挿入を行う関数
    def insert_block(self, isNum=None):
        return self.insert_block_af()
        # 元ソースコードから挿入する(親となる)部分を選択(code_block:make_block型)
        # 置換の場合(insert_idが更新されている場合)は、削除した部分のidを取得
        insert_id = self.temp_id
        # self.insert_parent = self.temp_id
        if insert_id == None:
            insert_id = self.getRandom_insert_num(self.mB_source)
            self.insert_parent = insert_id
            # self.logger.info("insert_id: " + str(insert_id))
            # self.logger.info(self.mB_source.set_parentable)
        # 以下、外部ソースコードに対しての操作
        # mB_exts：外部ソースコードブロックの配列
        # 複数の外部ソースコードのうち、挿入するソースコードを選択
        exts_num = len(self.mB_exts)
        # 挿入するコードを選択　例：[ext1, ext2, ext3, ext4]
        # ここでおかしくなってた！！
        # 0から始めないとね！！
        sel_num = self.getRandom_source_num(exts_num, True)
        self.ext_id = sel_num
        # ソースコードをブロックとして取得
        code_block_ext = self.mB_exts[sel_num]
        # ソースコードの部分をASTとして取得
        # ブロックをテキスト化する
        # 外部ソースコードから挿入する部分を選択
        # 0以上cnt未満の乱数を取得(挿入する必要ないので、どこでもok)
        # そんなことないよ！！宣言文は追加しちゃダメって先輩言ってたよ！！
        # ext_num = self.getRandom_source_num(code_block_ext.cnt, True)
        # o ：ステートメントを持つステートメントの選択
        # o ：ステートメントを持たないステートメントの選択
        # x ：宣言文の選択
        # insert_numだとステートメントを持つだけをせんたくしてしまうので修正
        # 外部から宣言部以外のブロックを取得
        without_D = code_block_ext.set_all - code_block_ext.set_decl
        ext_num = self.getRandom_from_set(without_D)
        self.insert_id = ext_num
        # ext_num 自身をテキスト化する。
        # モジュール全体であれば、全体のテキストにする。
        # ===================================================================
        # ===========================TODO====================================
        # ================識別子・変数名の識別子を取得する====================
        # ======この抽出した外部ソースコードにはどんな変数名があるのか=========
        # ===================================================================
        # ==================スコープIdについても考えよう！！==================
        # ===================================================================
        mB_source_names = self.mB_source.dic_type2name
        self.logger.info("mB_source_names: " + str(mB_source_names))
        # ここで取得したものが条件式だけの可能性があるので、子どもの確認をしていたら追加しよう！
        self.logger.info(code_block_ext.dic_stats)
        print(ext_num, code_block_ext.dic_tree)
        list_ext_ast = code_block_ext.dic_stats[ext_num]

        # 最初に加えるときは改行する。
        isN = True
        if ext_num == 0:
            # モジュール全体のとき
            pass
        elif ext_num in code_block_ext.dic_tree:
            # 子どもを持っている場合は list_ext_ast に子どもを追加する
            # 配列で取得される
            chi_nums = code_block_ext.dic_tree[ext_num]
            for chi_num in chi_nums:
                if isN:
                    list_ext_ast.append("\n")
                    isN = False
                chi_asts = code_block_ext.dic_stats[chi_num]
                # 辞書はリスト型
                """for chi_ast in chi_asts:
                    # ここのタブでバグが発生：いれる部分のインデント
                    list_ext_ast.append("\t")
                    list_ext_ast.append(chi_ast)"""

        self.logger.info(code_block_ext.dic_stats)
        self.logger.info(list_ext_ast)

        length = len(list_ext_ast)
        self.logger.info("list_ext_ast: " + str(list_ext_ast))
        # list_ext_ast のASTを変更する
        for i in range(length):
            code_ext_ast = list_ext_ast[i]
            # 全てのスーパークラスを取得する
            # self.logger.info(type(code_ext_ast).__mro__)
            import ast
            if ast.AST in type(code_ext_ast).__mro__:
                # ==================================================
                # =====================TODO=========================
                # =====astを下って、Name(変数名)の有無を確認する=====
                # ======code_ext_ast が astオブジェクトの場合=======
                # =========== 変数名の確認と置換をしたい ===========
                # ==================================================
                import change_name

                # self.logger.info("RB.py 113行目でexitする")
                # self.logger.info("code_ext_ast: " + str(code_ext_ast))
                # self.logger.info("code_block_ext: " + str(code_block_ext))
                # list_ext_astを更新する
                list_ext_ast[i] = change_name.change_name(
                    code_ext_ast, self.mB_source, code_block_ext, 0  # 外部のid
                )
                # exit()

            # 取得した要素がASTではない場合
            else:
                continue

        # self.logger.info(list(ast.walk(code_ext_ast)))

        # テキストの管理は不要
        '''txt_ext = ""
        if ext_num == 0:
            txt_ext = code_block_ext.return_code()
        # それ以外の場合は子どもを確認して、合体させる
        else:
            # self.logger.info(code_block_ext.dic_tree)
            txt_ext += code_block_ext.return_code(ext_num)
        '''
        # 辞書に追加するのは、テキスト化ではなく、AST！
        # ブロックのステートメントにidを付与する
        # これをやめる：mB L230で更新をしているため、ここで調整
        ext_id = self.mB_source.getNum()
        # ext_id = self.mB_source.cnt
        # 外部idをステートメント一覧に追加
        # ex) list_ext_ast = ['if ', <_ast.BoolOp object at 0x000001C1DF223220>, ':']
        self.mB_source.dic_stats[ext_id] = list_ext_ast
        # self.logger.info(self.mB_source.dic_stats)
        # self.logger.info("テキスト化: " + str(code_block_ext.return_code()))

        # insert_idと外部_idの親子関係を辞書に追加
        self.mB_source.set_dic_tree_append(ext_id, insert_id)
        self.logger.info("insert_id: " + str(insert_id))
        self.logger.info("ext_id: " + str(ext_id))
        # スコープIdを更新する
        # self.logger.info(self.mB_source.sIds)
        # self.mB_source.set_ScorpIds()
        # self.logger.info(self.mB_source.sIds)
        self.logger.info(self.mB_source.dic_stats)
        
        """for i in range(self.mB_source.cnt + 1):
            list_as = self.mB_source.dic_stats[i]
            import astunparse
            for s in list_as:
                # ASTかどうかを
                if ast.AST in type(s).__mro__:
                    print(astunparse.unparse(s), end="")
                else:
                    print(s, end="")
            print()"""

        # exit()
    # """

    #　置換後の挿入を行う関数
    def insert_block_af(self, isNum=None):
        # isNumは置換の場合のみidが入っている

        # 元ソースコードから挿入する(親となる)部分を選択(code_block:make_block型)
        # 置換の場合(insert_idが更新されている場合)は、削除した部分のidを取得
        # insert_id = self.temp_id
        # self.insert_parent = self.temp_id
        insert_id = isNum
        self.insert_parent = isNum
        
        # 置換ではない場合、挿入する部分を選択
        if insert_id == None:
            insert_id = self.getRandom_insert_num(self.mB_source)
            self.logger.info("insert_id " + str(insert_id))
            # 八百長
            insert_id = self.yao.update_insert_id(insert_id)
            self.insert_parent = insert_id
            
        # 以下、外部ソースコードに対しての操作
        # mB_exts：外部ソースコードブロックの配列
        # 複数の外部ソースコードのうち、挿入するソースコードを選択
        exts_num = len(self.mB_exts)
        # 挿入するコードを選択　例：[ext1, ext2, ext3, ext4]
        # ここでおかしくなってた！！
        # 0から始めないとね！！
        # self.logger.info("外部ソースコードの選択：" + str(exts_num))
        # exit("Repair_block 326:exit")
        sel_num = self.getRandom_source_num(exts_num, True)
        # 八百長
        sel_num = self.yao.update_sel_num(sel_num)
        self.ext_id = sel_num
        
        # ソースコードをブロックとして取得
        code_block_ext = self.mB_exts[sel_num]
        # ソースコードの部分をASTとして取得
        # ブロックをテキスト化する
        # 外部ソースコードから挿入する部分を選択
        # 0以上cnt未満の乱数を取得(挿入する必要ないので、どこでもok)
        # そんなことないよ！！宣言文は追加しちゃダメって先輩言ってたよ！！
        # ext_num = self.getRandom_source_num(code_block_ext.cnt, True)
        # o ：ステートメントを持つステートメントの選択
        # o ：ステートメントを持たないステートメントの選択
        # x ：宣言文の選択
        # insert_numだとステートメントを持つだけをせんたくしてしまうので修正
        # 外部から宣言部以外のブロックを取得
        without_D = code_block_ext.set_all - code_block_ext.set_decl
        ext_num = self.getRandom_from_set(without_D)
        # 八百長
        ext_num = self.yao.update_ext_num(ext_num)
        self.insert_id = ext_num
        # ext_num 自身をテキスト化する。
        # モジュール全体であれば、全体のテキストにする。
        # ===================================================================
        # ===========================TODO====================================
        # ================識別子・変数名の識別子を取得する====================
        # ======この抽出した外部ソースコードにはどんな変数名があるのか=========
        # ===================================================================
        # ==================スコープIdについても考えよう！！==================
        # ===================================================================
        mB_source_names = self.mB_source.dic_type2name
        self.logger.info("mB_source_names: " + str(mB_source_names))
        # ここで取得したものが条件式だけの可能性があるので、子どもの確認をしていたら追加しよう！
        self.logger.info(code_block_ext.dic_stats)
        # 2 {0: [1, 3], 3: [2, 5], 2: [4], 5: [6]}
        print(ext_num, code_block_ext.dic_tree)
        # exit("Repair_Block.py:310")
        list_ext_ast = code_block_ext.dic_stats[ext_num]

        isN = True
        # 挿入する外部ソースコードのブロックを、リストにする。
        if ext_num == 0:
            # モジュール全体のとき
            pass
        elif ext_num in code_block_ext.dic_tree:
            # 子どもを持っている場合は list_ext_ast に子どもを追加する
            """
            # ここは不要
            chi_nums = code_block_ext.dic_tree[ext_num]
            for chi_num in chi_nums:
                if isN:
                    list_ext_ast.append("\n")
                    isN = False
                chi_asts = code_block_ext.dic_stats[chi_num]
                # 辞書はリスト型
                for chi_ast in chi_asts:
                    # ここのタブでバグが発生：いれる部分のインデント
                    list_ext_ast.append("\t")
                    list_ext_ast.append(chi_ast)"""

        # """

        self.logger.info(code_block_ext.dic_stats)
        # self.logger.info(list_ext_ast)

        # length = len(list_ext_ast)
        # self.logger.info("list_ext_ast: " + str(list_ext_ast))
        # list_ext_ast のASTを変更する
        # for i in range(length):
        # obj_all = list_ext_ast[0]
        # この数は、外部ソースコードの中のid
        ext_num = ext_num
        # new_obj_all = self.cahnge_ast_name(obj_all, code_block_ext)

        # self.logger.info(list(ast.walk(code_ext_ast)))

        # テキストの管理は不要
        """txt_ext = ""if ext_num == 0:txt_ext = code_block_ext.return_code()# それ以外の場合は子どもを確認して、合体させるelse:# self.logger.info(code_block_ext.dic_tree)txt_ext += code_block_ext.return_code(ext_num)"""
        # 辞書に追加するのは、テキスト化ではなく、AST！
        # ブロックのステートメントにidを付与する
        # 外部ソースコードの子供がいる場合は、それも追加する
        self.logger.info(self.mB_source.dic_stats)
        self.insert_Main(ext_num, code_block_ext, insert_id)

        self.logger.info(self.mB_source.dic_stats)
        # exit()

        # スコープIdを更新する
        self.logger.info(self.mB_source.sIds)
        # self.mB_source.set_ScorpIds()
        self.logger.info(self.mB_source.sIds)
        # exit()

    def insert_Main(self, ext_num, code_block_ext, insert_id):
        self.logger.info("insert_Main")
        self.logger.info("ext_num: " + str(ext_num))
        self.logger.info("insert_id: " + str(insert_id))
        self.logger.info("code_block_ext.dic_tree: " +
                         str(code_block_ext.dic_tree))
        # とりあえず自身を変更する
        # 改善済み： insert_id: 2,5,9のとき無限ループ
        # insert_id = mBで親になるid
        # 修正対象コードに対しての外部ソースコードのid
        ext_id = self.mB_source.getNum()
        self.insert_ast(ext_num, code_block_ext, insert_id, ext_id)

        # 子供を持っている確認 = 親になっているかどうか
        isChild = (ext_num in code_block_ext.dic_tree)
        # self.logger.info("ext_num in code_block_ext.dic_tree: " + str(isChild) + " " + str(ext_num))
        # self.logger.info("code_block_ext.dic_tree: " + str(code_block_ext.dic_tree))
        # self.logger.info(str(isChild))
        while isChild:
            # print("-"*100)
            # self.logger.info("code_block_ext.dic_tree: " + str(code_block_ext.dic_tree)  + " " + str(ext_num))

            # 自分自身のidを設定する
            # 修正対象コードに対しての外部ソースコードのid
            # ext_id = self.mB_source.getNum()
            # 変更後のオブジェクトを追加する
            ext_list = code_block_ext.dic_stats[ext_num]
            self.mB_source.dic_stats[ext_id] = ext_list
            print("ext_list: " + str(ext_list))
            # insert_idと外部_idの親子関係を辞書に追加

            self.mB_source.set_dic_tree_append(ext_id, insert_id)
            # self.logger.info("親: " + str(insert_id) + " " + str(self.mB_source.dic_stats[insert_id]))
            # self.logger.info("子: " + str(ext_id) + " " + str(self.mB_source.dic_stats[ext_id]))

            # self.logger.info(str(ext_num) + " " + str(code_block_ext.dic_tree))
            # このext_idの子を持っているかどうか。
            children = code_block_ext.dic_tree[ext_num]

            # self.logger.info("ext_num: " + str(ext_num) + " → " + "children: " + str(children))
            # code_blockの中
            for child_id in children:
                # print("*"*100)
                # self.logger.info(str(ext_num) + " " + str(child_id)+ " " + str(code_block_ext)+ " " + str(ext_id))
                self.insert_Main(child_id, code_block_ext, ext_id)

            isChild = (ext_num in code_block_ext.dic_tree)
            # self.logger.info("ext_num in code_block_ext.dic_tree: " + str(isChild)  + " " + str(ext_num))
            isChild = False

        self.logger.info("self.dic_tree: " + str(self.mB_source.dic_tree))
        # exit()

    def insert_ast(self, ext_num, code_block_ext, insert_id, ext_id):
        self.logger.info(
            "*********************　insert_ast　*********************")
        self.logger.info("ext_num: " + str(ext_num))
        self.logger.info("ext_code: " + str(code_block_ext.dic_stats[ext_num]))
        # ext_d = self.mB_source.cnt
        # 外部idをステートメント一覧に追加
        # ex) list_ext_ast = ['if ', <_ast.BoolOp object at 0x000001C1DF223220>, ':']
        # ['if ', <_ast.BoolOp object at 0x00000276EA6D9280>, ':']
        # print(ext_list)
        # {1: 0, 3: 0, 2: 3, 4: 2, 5: 3, 6: 5}
        # print(code_block_ext.dic_children)
        ext_list = code_block_ext.dic_stats[ext_num]
        for i, ext_ast in enumerate(ext_list):
            # 変数名の変更をする
            # ext_ast = ext_list[i]
            ext_list[i] = self.cahnge_ast_name(ext_ast, code_block_ext)
        # self.logger.info(self.mB_source.dic_stats)
        # self.logger.info("テキスト化: " + str(code_block_ext.return_code()))

        # 変数名を変更したオブジェクトを追加する。
        # ext_list
        # print(ext_num, insert_id, ext_id, code_block_ext,)
        # ext_num   ：外部のソースコードについてのid
        # insert_id ：挿入する、修正対象コードの親となるid
        # ext_id    ：修正対象コードの子となる、外部コードのid

        self.mB_source.dic_stats[ext_id] = ext_list
        print("ext_list: " + str(ext_list))
        # insert_idと外部_idの親子関係を辞書に追加

        self.mB_source.set_dic_tree_append(ext_id, insert_id)
        self.logger.info("親: " + str(insert_id) + " " +
                         str(self.mB_source.dic_stats[insert_id]))
        self.logger.info("子: " + str(ext_id) + " " +
                         str(self.mB_source.dic_stats[ext_id]))

        self.logger.info(str(ext_num) + " " + str(code_block_ext.dic_tree))

    # 置換を行う関数

    def replace_block(self):

        # 最初に削除を行う
        # 全体を削除しても置換の場合はok
        # 置換なのでisRep=True
        self.delete_block(True, True)
        # 挿入を行う
        self.logger.info("置換を行う")
        self.logger.info(self.mB_source.dic_tree)
        # self.logger.info(self.temp_id)
        # 置換をするとき、temp_idは親から外されるので、temp_idの親を取得する
        # 事前にtemp_idを取得しておく
        # parent_temp = self.mB_source.dic_children[self.temp_id]
        # self.logger.info("parent_temp: " + str(self.temp_id) + " "+ str(self.temp_id))
        # exit()
        self.insert_block_af(self.temp_id)
        self.logger.info(self.mB_source.dic_tree)
        # exit("RB.py 158行目でexitする")

        """if self.temp_id == 0:
            self.logger.info("置換後のコード")
            # 自分自身を参照してしまっているので、修正
            # self.mB_source.dic_tree{0: [0]}
            # self.mB_source.dic_children{0: 0}
            self.mB_source.dic_tree = dict()
            self.mB_source.dic_children = dict()
            # self.logger.info(self.mB_source.return_code())
            # exit()
        """

    # ASTの変数名を変える関数
    # 引数：変数名を変えるオブジェクト、外部のブロック
    def cahnge_ast_name(self, code_ext_ast, code_block_ext):
        # code_ext_ast = list_ext_ast[i]
        # ['if ', <_ast.BoolOp object at 0x0000017DA2F08280>, ':', '\n', '\t', <_ast.Expr object at 0x0000017DA2F08340>]
        self.logger.info("code_ext_ast: " + str(code_ext_ast))

        # 全てのスーパークラスを取得する
        # self.logger.info(type(code_ext_ast).__mro__)
        import ast
        if ast.AST in type(code_ext_ast).__mro__:
            # ==================================================
            # =====================TODO=========================
            # =====astを下って、Name(変数名)の有無を確認する=====
            # ======code_ext_ast が astオブジェクトの場合=======
            # =========== 変数名の確認と置換をしたい ===========
            # ==================================================
            import change_name

            # self.logger.info("RB.py 113行目でexitする")
            # self.logger.info("code_ext_ast: " + str(code_ext_ast))
            # self.logger.info("code_block_ext: " + str(code_block_ext))
            # list_ext_astを更新する
            code_ext_ast = change_name.change_name(
                code_ext_ast, self.mB_source, code_block_ext, 0  # 外部のid
            )
            return code_ext_ast
            # exit()

        # 取得した要素がASTではない場合
        # 何も変換s寝ずに、そのまま返す
        else:
            return code_ext_ast

    # ブロックを修正して、修正したコードを返します

    def repair(self, gen_num):
        #rep_code = None
        # while rep_code == None:
        self.logger.info(self.mB_source.sIds)

        # 削除 / 置換 / 挿入をランダムで行う
        self.logger.info("start_Repair")
        self.logger.info("dic_stats: " + str(self.mB_source.dic_stats))
        self.logger.info("dic_children: " + str(self.mB_source.dic_children))
        self.logger.info("dic_tree: " + str(self.mB_source.dic_tree))
        
        # 方法一覧からランダムに選択
        import random
        rep_ways = ["insert", "delete", "replace"]
        way_num = random.randint(0, len(rep_ways) - 1)
        # 選択された修正方法
        # 八百長：置換のみ
        way_num = self.yao.update_way_num(way_num)
        rep_way = rep_ways[way_num]
        file = open(r"way_result.csv", "a")
        file.write(str(gen_num) + ":" + str(rep_way) + "\n")
        file.close()
        
        print("rep_way **************** ",rep_way)
        
        # 統計的に選択されたのを見ておきたいので記録する
        self.way = rep_way
        # コマンドように変換
        rep_way += "_block"
        # 何らかの操作を行う
        # ここを変更して確認などを行う！
        # print("Repair.py 205行目でexitする", self.mB_source.cnt)
        eval("self." + rep_way + "()")
        # print("Repair.py 205行目でexitする", self.mB_source.cnt)
        # 変更後に更新をする
        import BFS
        print("526", self.mB_source.dic_tree)
        # 木を調整する(同じidは2つ以上子になれない)
        self.adjust_tree()
        
        #print("574", self.mB_source.dic_tree)
        #print("574", self.mB_source.dic_children)
        
        """print("bef", self.mB_source.sIds)
        # print(BFS.main_update(self.mB_source.dic_tree, self.mB_source.cnt))
        self.mB_source.sIds = BFS.main_update2(
            self.mB_source.dic_tree, self.mB_source.cnt
        )
        print("aft",self.mB_source.sIds)
        # exit()
        
        for i in range(self.mB_source.cnt):
            print(i, self.mB_source.sIds[i], self.mB_source.dic_stats[i])"""
        # exit()
        # eval("self." + rep_ways[0] + "()")
        # 記憶していたものを初期化
        self.temp_id = None
        # 世代のデバッグ
        self.logger.info("gen_num: " + str(gen_num))

        # self.mB_source
        
        # exchangeB = ast2lang.exchange_Block(self.mB_source)
        # print(ast2lang.return_All_code(self.mB_source))
        # 修正したコードが文法的に正しいか
        # exit(self.mB_source.input_path)
        #
        
        print(self.mB_source.sIds)
        self.mB_source.sIds = BFS.main_update2(self.mB_source.dic_tree, self.mB_source.cnt)
        # print(rep_code)
        # print("-" * 90)
        print(self.mB_source.sIds)
        
        """for i in range(len(self.mB_source.sIds)):
            print(i,self.mB_source.dic_stats[i])
        """
        rep_code = ast2lang.return_All_code(self.mB_source)
        # print(rep_code)
        # exit("Repair.py 605行目でexitする")
        
        # 返却したコード
        # print(rep_code)
        # exit("exit315")
        # 正しくない場合はNoneが返ってくる
        return rep_code

    def adjust_tree(self):
        dic_bef = self.mB_source.dic_tree
        dic_aft = dict()
        for key in dic_bef.keys():
            # 重複可能性有り
            vals_list = dic_bef[key]
            # 重複削除して、昇順リストにする
            val_list = sorted(list(set(vals_list)))
            dic_aft[key] = val_list
        self.mB_source.dic_tree = dic_aft