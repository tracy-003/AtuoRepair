import ast
from collections import deque
from langs2ast.java import Java2ast00
import heapq
import copy
import queue


class Main():
    def __init__(self, word_list):
        self.word_list = word_list
        self.num_blankPair = 0

    # これを呼び出し！
    def return_astTree(self):
        # wordlistから識別子の優先度などを取得する。
        # 返却値：(asオブジェクト, 優先度)
        # que_obj：優先度とオブジェクトのタプルのキュー
        # que_pri：優先度のキュー
        que_obj, que_pri = self.ex_token()
        # print(">>>>>", que_pri)
        # print("que_obj", que_obj)
        # print("que_pri", que_pri)
        object = self.make_ast_expr(que_obj, que_pri)
        print("26")

        return object

    # キューを返却する(キューの要素は、(astオブジェクト, 優先度))
    def ex_token(self):
        # FIFO
        q_words = deque()
        heap_list = []
        for s in self.word_list:
            tuple_obY = Java2ast00.return_objY(s)
            q_words.append(tuple_obY)
            # print(tuple_obY[0], (type(tuple_obY[0]).__bases__))
            # 優先度の値
            
            num_pri = tuple_obY[1]
            
            # 優先度から括弧の数を計算する。
            if num_pri == 40:
                self.num_blankPair += 1
                # スタートの優先度はいらないので、elifにする。

            # 最大値を求めるために入力値に-1をかける。
            elif num_pri > 0:
                # https://qiita.com/ell/items/fe52a9eb9499b7060ed6
                num_pri *= -1
                heap_list.append(num_pri)

        # 優先度を優先度付きキューにする
        heapq.heapify(heap_list)
        # print(q_words)
        # 優先度の高いやつが先に出てくる
        # print(heap_list.pop())
        # print("q_words", q_words)
        # q_words deque([(<_ast.Name object at 0x000001F05DAB8550>, 0), (<_ast.LtE object at 0x000001F05DB4B7F0>, 7), (<_ast.Constant object at 0x000001F05DBDA1C0>, 0), (<_ast.BoolOp object at 0x000001F05DBDA460>, 12), ('', 20), (<_ast.Name object at 0x000001F05DBF91F0>, 0), (<_ast.Add object at 0x000001F05DBF9280>, 5), (<_ast.Constant object at 0x000001F05DBF9250>, 0), ('', 21), (<_ast.Eq object at 0x000001F05DBF9340>, 8), (<_ast.Constant object at 0x000001F05DBF9370>, 0)])
        # print("heap_list", heap_list)
        # heap_list [5, 7, 8, 12, 21, 20]
        return q_words, heap_list

    # 括弧を探して一塊にする。
    def update_que(self, stack_result, stack_exchan):
        # 引数；今までの結果 stack_result
        # 計算用に使うリスト構造 stack_exchan
        # 「(」までスタックを取り出す。
        isBlack_S = False
        que_pri_ex = []
        while not(isBlack_S):
            obj = stack_result.pop()
            if obj[0] == "(":
                isBlack_S = True
            else:
                stack_exchan.append(obj)
                pri = obj[1]
                if pri > 0:
                    que_pri_ex.append(pri)

        # stack_exchan をASTに変換する。
        # print("stack_exchan", stack_exchan)
        heapq.heapify(que_pri_ex)
        # print("que_pri_ex", que_pri_ex)
        ast_obj = self.make_ast_expr(stack_exchan, que_pri_ex)
        # print("ast_obj", ast_obj)
        stack_result.append((ast_obj, 0))
        return stack_result, stack_exchan

    # 括弧をなくしたい！
    def update_blank(self, que_obj, que_pri):
        # 括弧がないときは、そのまま返却する。
        print("優先度付きキューは、", que_pri, "です。")
        # 括弧が含まれていなかったら、そのまま返却する。
        if len(que_pri) > 0:
            max_pri = heapq.heappop(que_pri)
        # 単語が一つ？？の時
        else:
            # かっこをなくさなくてもよき！！
            print("que_obj", que_obj)
            return que_obj, que_pri


        # 優先度    
        if -40 < max_pri and max_pri < 40:
            # print("makeAST_JavaExpr.py：", que_obj, "は括弧を含んでいません。")
            # 間違えて取っちゃったので、戻す。
            # print("93行目：", que_pri)
            heapq.heappush(que_pri, max_pri)
            # print("95行目：", que_pri)
            return que_obj, que_pri

        print("que_obj", que_obj)
        # for i, q in enumerate(que_obj):
            # print(i, q)
        """print("que_pri")
        print(self.num_blankPair)
        exit()"""
        # 終端までのストック
        stack_proc = deque()
        # 参考：単純な構文解析をjavaで実装する
        # https://qiita.com/quwahara/items/9bf468ff4286b28d2a24
        # ×：優先度の高いものから取り出す。
        # 括弧の優先度は高い：40,41
        # それ以外の優先度は優先度が高いほど、小さい値になる。
        # かっこの処理
        for i in range(self.num_blankPair):
            # 最大値の取り出し
            heapq.heappop(que_pri)
            # 終端記号
            isBlank_End = False
            # 終端までのストック
            # stack_proc = deque()
            # 終端を探す
            while not(isBlank_End):
                obj_tupl = que_obj.popleft()
                if obj_tupl[0] == ")":
                    isBlank_End = True
                else:
                    # print("この値：", obj_tupl)
                    stack_proc.append(obj_tupl)
            # 終端が見つかったら、stack_procの(までを変換する。
            isBlank_Start = False
            # 変換対象のキューと優先度のキュー
            que_ex = deque()
            que_ex_pri = []
            
            print("*****" * 10, "stack_proc", "*****" * 10)
            # print(stack_proc)
            # for s in stack_proc:
            #    print("obj",s[0])
                
            while not(isBlank_Start):
                obj_tupl = stack_proc.pop()

                # シンボルで判断する。
                if obj_tupl[0] == "(":
                    isBlank_Start = True
                else:
                    que_ex.appendleft(obj_tupl)
                    # 優先度が0でないときに追加する
                    # 追加条件：「(」では、ないとき。
                    if obj_tupl[1] != 0:
                        que_ex_pri.append(obj_tupl[1])

            # 変換対象のキューを変換する。
            # print("128", "que_ex", que_ex_pri)
            heapq.heapify(que_ex_pri)
            # ["x", "%", "4"] の変換結果
            # que_obj deque([(<_ast.Name object at 0x000001A5867080D0>, 0), (<_ast.Mod object at 0x000001A58682A190>, 4), (<_ast.Constant object at 0x000001A586A4B760>, 0)])
            # que_pri [-4]
            # print(que_ex)
            # print(que_ex_pri)
            # exit("exit:144")
            aft_que = self.make_ast_expr(que_ex, que_ex_pri)

            # 変換後のオブジェクトをque_objに追加する。
            # que_obj.append((aft_que, 0))
            stack_proc.append((aft_que, 0))
            
        # 括弧1つ分削除
        # print("1個 削除")
        # print(stack_proc)
        
        # 括弧を処理した。あと
        # print("残った後の括弧の確認です！！")
        # スタックについか
        for tup_rr in que_obj:
            stack_proc.append(tup_rr)
        # exit()
        # print("↓" * 150)
        # print("stack_proc")
        que_obj = deque()
        for q in stack_proc:
            que_obj.append(q)
            
        # print("que_pri", que_pri)
        # exit("155:exit")
        
        # print("163:que_obj", que_obj)
        que_pri = []
        for tup_obj in que_obj:
            if tup_obj[1] != 0:
                que_pri.append(tup_obj[1])
        
        return que_obj, que_pri

    # キューからastオブジェクトを作成する
    def make_ast_expr(self, que_obj, que_pri):
        # print(210)
        que_obj, que_pri = self.update_blank(que_obj, que_pri)
        # print("かっこを処理した後のque_obj", que_obj)

        # print("173:que_obj", que_obj)
        # print("174:que_pri", que_pri)

        # print(217)

        """# かっこの処理を行う。
        cnt_brank = -1
        max_pri = 41
        # )の数をカウントする。
        
        print(">>>>", que_obj)

        while max_pri == 41:
            # 最大値の取り出し
            # print(que_pri, "から")
            max_pri = heapq.heappop(que_pri)*(-1)
            # print("max_pri", max_pri)
            cnt_brank += 1
        # 間違えて撮ったものを戻す
        heapq.heappush(que_pri, max_pri)
        # 「(」の優先度をクリーンにする。
        for i in range(cnt_brank):
            heapq.heappop(que_pri)*(-1)
         # キューの先頭の要素を取り出す
        stack_result = deque()  # collections.deque（append(), pop()）
        # 変換するときにいれるスタック(リスト構造にしておくよ！)
        # やっぱり、deque()にする！！
        for i in range(cnt_brank):
            # 今までの結果をいれていくスタック
            stack_exchan = deque()
            isBlank_s = False
            while not(isBlank_s):
                tuple_obY = que_obj.popleft()
                # 単語が「)」かどうかを判定する。
                word = tuple_obY[0]
                if word == ")":
                    # 「）」が来たら更新をする
                    stack_result, stack_exchan = self.update_que(stack_result, stack_exchan)
                    isBlank_s = True
                    print("stack_result", stack_result)
                    # print("stack_exchan", stack_exchan)
                    # exit()
                    # que_obj.append(stack_result)
                else:
                    stack_result.append(tuple_obY)

        """
       
        # 今度は、優先度の低い方から探索するので、-1を書ける。
        # que_pri = list(map(lambda x: x*(-1), que_pri))  # 各要素を-1倍
        heapq.heapify(que_pri)  # ヒープ化をする

        # print(266)

        # 保存用のキュー
        temp_que = deque()
        # que_obj の要素数が1になるまで繰り返す
        # while len(que_obj) > 1:
        # 優先度キューがなくなるまで繰り返す
        while len(que_pri) > 0:
            """for i, tupl in enumerate(que_obj):
                print(i, tupl)"""
            # 目標の優先度(低い方から)
            # print("que_pri", que_pri, len(que_obj) > 1)
            # print(que_pri)
            target_pri = heapq.heappop(que_pri)
            # print("最初に選ばれた優先度", target_pri)
            # ×：目標が負の時は、正にする！
            # ○：目標がせいの時は、負にする！
            # → 負にすることで数値の低いもの(優先度の高いもの)が取り出せる。
            # 取り出したものの調整が必要な場合
            if target_pri > 0:
                # 一回戻してから、負にする。
                heapq.heappush(que_pri, target_pri)
                # target_pri *= -1
                # print("before que_pri", que_pri)
                # print(target_pri,"優先度be",que_pri)
                # 一気に負にする
                que_pri = list(map(lambda x: x*(-1), que_pri))
                # リストをヒープ化！！
                heapq.heapify(que_pri)
                # print("after que_pri", que_pri)
                # 負にしてから取り出す。
                target_pri = heapq.heappop(que_pri)
                # print(target_pri,"優先度af",que_pri)
            
            # target_pri が負だとそりゃ見つからないよね。
            if target_pri < 0:
                target_pri *= -1

            # print("優先度の高い方から(数値的には高くした)", target_pri, "残りの優先度", que_pri)
            # que_objが空になるまで
            # print("209", que_obj, que_pri)
            while len(que_obj) > 0:
                # print("272", len(que_obj), que_obj)
                # for i in range(len(que_obj)):
                # キューの先頭の要素を取り出す
                tuple_obY = que_obj.popleft()
                # print("tuple_obY", tuple_obY)
                # 優先度を取り出す
                num_pri = tuple_obY[1]
                # 優先度が目標の優先度と同じならば
                # print("temp_que", temp_que)
                if num_pri == target_pri:
                    # 値の取得
                    # 最初の数(a%4のa)を取り出す
                    obj_f = temp_que.pop()[0]
                    # 演算子
                    obj_en = tuple_obY[0]
                    # rint("演算子", obj_en)
                    # 次の数(a%4の4)を取り出す
                    obj_l = que_obj.popleft()[0]
                    # print(obj_f)
                    # print(obj_en)
                    # print(obj_l)
                    # 式に変換
                    # この演算子は
                    # opか、cmpopか、boolopか、unaryopか
                    # type_en = type(tuple_obY[0]).__bases__
                    # print(type_en, type_en is ast.operator)
                    # 取り出したオブジェクトはoperatorのサブクラス
                    #print(issubclass(type(tuple_obY[0]), ast.operator))
                    # 式を組み立ててから
                    # 保存用のキューに入れる
                    # オペレーターの場合
                    # print("オペレーター？", issubclass(type(tuple_obY[0]), ast.operator))
                    if issubclass(type(tuple_obY[0]), ast.operator):
                        ast_obj = ast.BinOp(obj_f, obj_en, obj_l)
                        # print(ast_obj)
                        # 式を生成したら、保存用のキューに入れる
                        # 優先度は0
                        temp_que.append((ast_obj, 0))
                        # import astunparse
                        # print(astunparse.unparse(ast_obj))

                    elif issubclass(type(tuple_obY[0]), ast.cmpop):
                        ast_obj = ast.Compare(obj_f, [obj_en], [obj_l])
                        # import astunparse
                        # print(astunparse.unparse(ast_obj))
                        # 式を生成したら、保存用のキューに入れる
                        # 優先度は0
                        temp_que.append((ast_obj, 0))

                    elif type(tuple_obY[0]) is ast.BoolOp:
                        # BoolOp(boolop op, expr* values)
                        tuple_obY[0].values = [obj_f, obj_l]
                        # 優先度は0
                        temp_que.append((tuple_obY[0], 0))

                    else:
                        # print("makeAST_JavaExpr.py:make_ast_expr:else")
                        e_obj = tuple_obY[0]
                        print("ここの型は未実装です >>", type(e_obj), ast.dump(e_obj))
                        # exit()

                else:
                    # 何もせずに保存用のキューに入れる
                    temp_que.append(tuple_obY)
            # return target_pri
            # 一旦終わったらtemp_queをque_objに戻す
            # temp_queをクリアする
            # print(que_obj, len(que_obj) > 1)
            # print("be", que_obj)
            que_obj = copy.copy(temp_que)
            # print("af", que_obj)
            # print(temp_que)
            # print(que_obj, len(que_obj) > 1)
            temp_que.clear()

        # print(383)

        # print("while 要素が1になった")
        # print(que_obj) # deque
        # print(temp_que)
        # タプル → astオブジェクト

        return que_obj[0][0]


if __name__ == '__main__':
    # test_list = ['y', '%', '400']
    # test_list = ['y', '%', '400', '==', '0']
    # test_list = ['y', '', '100', '==', '0']
    test_list = ['3.0', '*' , 'y', '/', '400', '==', '0']
    # 全部置換：違う構造のデータをもとめる
    # エラー１：解消済み
    # test_list = ['y', '<=', '5', '||', 'y' , '%', '3', '==', '0']
    # test_list = ['y', '<=', '10', '&&', 'y' , '%', '3', '==', '0']
    # エラー２
    # test_list = ['3', '==', '(', 'y', '%', '4', ')']
    # test_list = [ '(', 'y', '%', '4', ')', '*', '(', 'y', '%', '4', ')', '==', '4']
    # test_list = ['y', '<=', '10', '&&', '(' , '(', 'y', '+', '3', ')', '==', '0', ')']
    # test_list = ['n','%' ,'400', '==', '0','||','(','n','%','100','!=','0','&&','n','%','4','==','0',')']
    test_list = [  '(','x', '+', '7', '*','(', 'y', '%', '4', ')', '*', '3',')', '%', '4', '==', '4']

    mainObj = Main(test_list)
    astO = mainObj.return_astTree()
    # print("=" * 100)
    # print(astO)
    # print(ast.dump(astO))
    # import astunparse
    # print("以下に式を出力します")
    # print(astunparse.unparse(astO))