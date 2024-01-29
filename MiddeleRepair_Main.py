# [[1, 1], [870108, 201890463153], [159410, 6776465962], [65843, 1156128457], [307121, 25152923253], [212443, 12035221696], [15, 60]],

# conda activate new_study

# 中間言語の実行するメインのプログラム
from base64 import encode
import json
import make_Block
import ast
import astunparse
import json
from logging import getLogger, config
import Repair_Block
import Check_json_case
import subprocess
import copy

import random

from Test_all import TestMain

import return_language
import lang2kaku

import datetime

import time

# ディレクトリの移動
import os 

def Test(output_Path, test_case, input_lang, logger):
    
    # 入力値が複数になったら変える
    # test_in, test_out = test_case
    # test_out = str(test_out) +"\n"
    # print("test1 ======")
    is_passed = TestMain.test(output_Path, test_case, input_lang)
    return is_passed
    # print("pythonのテストを実行しています。")
    # print(is_passed)
    # exit(is_passed)
    try:
        ans = subprocess.run(
            ['python', output_Path]
            # ['python', 'PY01\\ou.py']
            , input = str(test_in) + "\n"
            , encoding="utf-8"
            , capture_output = True
            , text = True # inputの確認
            , timeout=5
        )
    except subprocess.TimeoutExpired:
        logger.warning("Timeout")
        # exit()
        return False
    # print("test2 ======")
    #logger.info("test_in:" + str(test_in))
    #logger.info("Test_out====" + str(str(test_out).split("\n")) + "====")
    #logger.info("Test_std====" + str(str(ans.stdout).split("\n")) + "====")
    #logger.info(str(test_out).startswith(str(ans)))
    #logger.info(str(str(test_out).split("\n")) == str(str(ans.stdout).split("\n")))
    # logger.info("ans.stdout:" + str(ans.stdout))
    # logger.info("test_out:" + str(test_out))
    
    #if ans.stdout == "":
    #    logger.warning("ans.stdout is empty")
    # print(str(ans.stdout) == (str(test_out) + "\n"))
    #exit()
    
    
    return str(ans.stdout) == str(test_out)

# テストを実行して、そのスコアや正答の真偽を返却します。
def return_test_score(_temp_Path, test_p_case, test_n_case, input_lang):
    # 保存したpyファイル(_temp_Path)を実行する。
    testP_results = []
    testN_results = []
    for test_case in test_p_case:
        isR = Test(_temp_Path, test_case,input_lang, logger)
        testP_results.append(isR)
    for test_case in test_n_case:
        isR = Test(_temp_Path, test_case, input_lang, logger)
        testN_results.append(isR)
    
    # テスト結果を計算する        
    test_score = testP_results.count(True) * test_p_score + testN_results.count(True) * test_n_score
    
    print("test_score",test_score)
    print("testP_results: ", testP_results)
    print("testN_results: ", testN_results)
    
    test_results = testP_results + testN_results
    
    return test_score, test_results

def cal_time(s_time_f):
    # 引数：float型の時間（単位：秒）
    # 小数点以下の秒数
    ms_time_i = int((s_time_f % 1) * 100)
    return_txt = "." + str(ms_time_i) + "秒"
    # 経過時間の秒数
    # print(s_time_f, int(s_time_f), int(s_time_f) % 60)
    s_time_i = int(int(s_time_f) % 60)
    # 経過時間を分数にしたもの(切り捨て)
    m_time_f = int(s_time_f // 60)
    
    return_txt = str(s_time_i) + return_txt
    
    """if m_time_f > 0:
        return_txt = str(s_time_i) + return_txt
    else:
        return "0" + return_txt
    """   
    # 経過時間の分数
    m_time_i = int(m_time_f % 60)
    if m_time_f > 0:
        return_txt = str(m_time_i) + "分" + return_txt
    
    # 経過時間の時間
    h_time_i = int(m_time_f // 60)
    if h_time_i > 0:
        return_txt = str(h_time_i) + "時間" + return_txt
        
    return return_txt

def main(input_Path, time_start,input_lang,target):
    rep_code = ""
    # メインの実行
    # 入力ファイル（pythonとかCなど）
    # testF = open(input_Path, encoding="UTF-8")
    # ファイルの文字コードを取得する
    # logger.info(testF.readlines())
    # ブロックの作成
    logger.info("Start")
    # input_Block = mB_source.main_return(logger, input_Path)
    # create make_Block
    # 修正対象コードをブロックにできるかどうか。
    # try:
    mB_source = make_Block.main(logger, input_Path)

    """except Exception as e:
    # print("Exceptoion")
        file = open(r"error_log.csv", "a")
        import traceback
        file.write(str(datetime.datetime.now()) + ":" + str(input_Path) + ":" + str(e) + "\n" + str(traceback.format_exc()) + "\n")
        print ('=== エラー内容 ===')
        print ('type:' + str(type(e)))
        print ('args:' + str(e.args))
        print ('message:' + e.message)
        # print ('e自身:' + str(e))
        import Send_Mail
        Send_Mail.send_message("makeBlockエラー", str(e))
        exit("makeBlockのエラーです")
        file.close()"""

    # return "", None, 0
    # print(input_Path)
    # ここにコードを載せる
    # logger.info(mB_source.dic_stats)
    # logger.info(mB_source.dic_tree)
    mB_source.print_Block(True)
    # exit()
    code_make_Block_source = mB_source.return_code()
    if code_make_Block_source is None:
        return 
    # else:
        # print("115", s)
        # ここで、されたコードを
    # exit("MiddleRepair_Main.py : exit116")
    """for i in range(mB_source.cnt + 1):
        print(i, mB_source.dic_stats[i])"""
    # exit("MiddeleRepair_Main.py:111:exit")
    
    ext_num = len(external_codes)
    
    # 外部コードをブロックに変換する。
    mB_exts = [None]*ext_num
    # 外部コードがからの時は、修正対象コードを追加する。
    if ext_num == 0:
        block_temp = copy.deepcopy(mB_source)
        mB_exts.append(block_temp)

    else:
        for i in range(ext_num):
            mB_exts[i] = make_Block.main(logger, external_codes[i])
            # print(external_codes[i])
            mB_ext_source = mB_exts[i]
            logger.info(mB_ext_source.dic_stats)
            #logger.info(mB_source.dic_tree)
            #logger.info(mB_source.dic_children)
            # exit()
            mB_ext_source.print_Block(True)
            # exit()
            
    # ブロックの表示
    mB_source.print_Block()
    # exit("MiddeleRepair_Main.py:129:exit")
    #for i in range(ext_num):
    #    mB_exts[i].print_Block()
    # exit("MiddeleRepair_main.py:126:ブロックの表示")
    
    
    # 外部ソースコードの識別子一覧を表示する
    """
    for bl_e in mB_exts:
        logger.info(bl_e.dic_identifier)
    """
    
    # テスト全部通るか
    isOk = False
    # その時点での最高得点
    now_score = -1 # 最初は-1（ずっと0の時は何も出力されないため）
    # 世代数
    gen_num = 0
    time_rep = 0
    # チェック済みかどうか
    is_first_check = False
    # ここでファーストチェックしたい！！
    while not(isOk) and (gen_num < max_gen) and (time_rep < 10000):
        # print("=" * 10000)
        # print(time_rep)
        # print("=" * 10000)
        gen_num += 1
        # 変更前のオブジェクトを記憶しておく
        temp_source = copy.deepcopy(mB_source)
        temp_exts = copy.deepcopy(mB_exts)
        temp_lists = [temp_source, temp_exts]
        # 変化させるファイル
        _temp_Path = "_output2" + lang2kaku.main(input_lang)
        print(_temp_Path, "に書き込みます。")
        
        # 最初のチェックをしよう！！！
        # if is_first_check:
        
        # 修正したコードをファイルに書き込む
        f = open(_temp_Path, "w", encoding="UTF-8")
        f.write(code_make_Block_source)
        f.close()
        # 全テストケースを実行する。
        test_score, test_results = return_test_score(_temp_Path, test_p_case, test_n_case, input_lang)
        # 改行設定ができたとき。
        if all(test_results):
            gen_num = -1
            return code_make_Block_source, None, -1        
        
        # 改行設定でできないときは、そのまま修正をする。

        # 深いコピーをしたブロックに対して修正を行う
        rep_code_object = None
        if not(is_first_check):
            rep_code_object = Repair_Block.Repair_Block(logger, temp_lists[0], temp_lists[1])
        # 修正したコードのテキストベース
        # 正しくない場合はNoneが返ってくる
        try:
            rep_code = rep_code_object.repair(gen_num)
        except Exception as e:
            # file = open(r"error_log.csv", "a")
            # import traceback
            # file.write(str(datetime.datetime.now()) + ":" + str(input_Path) + ":" + str(e) + "\n" + str(traceback.format_exc()) + "\n")
            print ('=== エラー内容 === MideeleRepair_Main.py:261')
            print ('type:' + str(type(e)))
            print ('args:' + str(e.args))
            print ('message:' + e.message)
            print ('e自身:' + str(e))
            """import Send_Mail
            Send_Mail.send_message("makeBlockエラー", str(e))
            exit("makeBlockのエラーです")"""
            # file.close()
            # rep_code = None

        # rep_codeがNoneの場合はもう一度修正を行う
        if rep_code == None:
            # なかったことにする
            gen_num -= 1
            time_rep = time.time() - time_start
        
        # rep_code が存在していたら…
        else:
            """if is_first_check:
            pass
        else:"""
            print(rep_code)
            # 修正したコードをファイルに書き込む
            f = open(_temp_Path, "w", encoding="UTF-8")
            f.write(rep_code)
            f.close()
            # 各世代の統計情報
            data = str(rep_code_object.way) + ","
            data += str(rep_code_object.del_num) + ","    # 削除したId
            data += str(rep_code_object.ext_id) + ","
            data += str(rep_code_object.insert_id) + "," # 挿入するId(文章)
            data += str(rep_code_object.insert_parent) # 挿入する親のId
            
            mB = rep_code_object.mB_source
            print("============================== MiddeleRepair_Main.py 225 ====================")
            print(mB.dic_stats)
            print(mB.dic_tree)
            print(data)

            
            # 修正したコードがもし空だったら
            if rep_code == "":
                logger.warning("修正したコードが空です。")
                # print(rep_code)
                break
            
            # 中間から直すときに確認済み
            # 修正したコードが文法的に正しいときは実行
            # if isRep:
            # print("MiddeleRepair_Main.py:rep_code, 73でexit!")
            # exit()
            
            
            # 全テストケースを実行する。
            test_score, test_results = return_test_score(_temp_Path, test_p_case, test_n_case, input_lang)
            #file = open(r"C:\Users\new_study\trans\make_middle\Result_score.txt", "a")
            #file.write(str(test_score) + "\n")
            #file.close()
            logger.info("test_score: " + str(test_score))

            # exit("test_soce：" + str(test_score))
            
            # testscoreが更新されたら更新する
            if test_score > now_score:
                # テストスコアを更新する
                now_score = test_score
                # ファイルをコピーする
                import shutil
                # test1をtest2にコピーする
                shutil.copyfile(_temp_Path, output_Path)
            
            print(test_results)
            
            isOk = all(test_results)
            
            print("isOk222: ", isOk)
            print(_temp_Path)
            print(rep_code_object.way)
            print("rep_code_object.del", rep_code_object.del_num)
            print("rep_code_object.ins_pa",rep_code_object.insert_parent)
            print("ext_id",rep_code_object.ext_id)
            # exit("1世代目が終わりました。")
            
            # 各世代の統計情報
            dic_ex = dict()
            dic_ex["insert"] = 0
            dic_ex["delete"] = 1
            dic_ex["replace"] = 2
            data = str(dic_ex[rep_code_object.way]) + ","
            data += str(rep_code_object.del_num) + ","    # 削除したId
            data += str(rep_code_object.ext_id) + ","
            data += str(rep_code_object.insert_id) + "," # 挿入するId(文章)
            data += str(rep_code_object.insert_parent) # 挿入する親のId

            file = open(r"Result_Generation.txt", "a")
            file.write(str(data) + "\n")
            file.close()

            print(not(isOk) and gen_num < max_gen and time_rep < 10000)
            # print(isOk)
            # exit()
        
                    
            # print("isOk230: ", isOk)

    
    # テストが通ったら(Whileが抜けたら)
    # テストの結果がOKならば修正したコードを入力ファイルに書き込む
    # ===> テストの得点が最も高いものを選ぶ
    if now_score == target:
        # 全てのテストケースがOKだったら、正しいコードを返す
        print("rep_code_object.way", rep_code_object.way)
        # exit()
        # logger.debug("修正方法" + str())
        #return rep_code
        #　コードと修正方法を返す
        print(rep_code)
        print(rep_code_object)
        print(gen_num)
        print(rep_code_object.way)
        print("rep_code_object.del", rep_code_object.del_num)
        print("rep_code_object.ins_pa",rep_code_object.insert_parent)
        print("ext_id",rep_code_object.ext_id)
        
        # print("-" * 10000)
        return rep_code, rep_code_object, gen_num
    
    else:
        # while文を抜けれない場合はもう1度修正する
        logger.warning("修正できませんでした")
        logger.info("現在の世代は、" + str(gen_num) + "です。")
        # 統計データを記録する。
        
        
        
    
    # 10000世代で修正できなかったら、その時点での最高のコードを返す
    # 最初にコメントなどを記述
    logger.warning(str(max_gen) + "世代で修正できませんでした")
    # f = open(output_Path, "r", encoding="UTF-8")
    # codes = "# unfinished\t"
    print(input_lang)

    codes = lang2kaku.return_com(input_lang)
    codes += "unfinished\t"
    # target：Check_json_case.pyの返却値
    codes += str(now_score) + "/" + str(target) + "\n"
    """for line in f.readlines():
        codes += line"""
    # f.close()
    codes += rep_code

    # 修正できなかった場合Noneを返す
    # 世代数はmaxを一応返す
    return codes, None, max_gen
    
    # after_block = rep.repair(logger, mB_source)
    
    # 修正後の中間言語(pythonに戻してもOK)
    # Python3.9で追加されたast.unparse()を使うと、ASTオブジェクトからソースコードを生成できます
    # import astunparse
    # print(astunparse.unparse(ast.parse(code)))
    

def setting_logFile(path):
    # ロガーの設定
    with open(path, 'r') as f:
        log_conf = json.load(f)
    config.dictConfig(log_conf)
    logger_set = getLogger(__name__)
    return logger_set

def start():
    # ディレクトリの移動
    # now_path = os.getcwd()
    # 現在のパスがstudyだったら、ディレクトリを変更する。
    
    # ログファイルの設定はif__name__内で
    """
    # ディレクトリの移動
    import os    
    path = os.getcwd()
    # logger.info("path: " + path)
    # ディレクトリの移動
    path = os.getcwd()
    """

def rep_Main(input_Path,output_Path):
    """if not (isEx):
        external_codes = []
    isEx = not (isEx)"""
    # パスが正しいかどうかの確認
    input_lang = return_language.language_from_Path(input_Path)
    
    # ログ
    logger.info("start checking %s", input_Path)
    
    if input_lang != return_language.language_from_Path(output_Path):
        logger.error("input_Pathとoutput_Pathのプログラミング言語が違います")
        exit(1)
    
    # jsonの設定が正しければ、上限のターゲットスコアが設定される
    target = Check_json_case.check(test_p_num,test_n_num ,test_p_case, test_n_case, test_p_score, test_n_score)
    if target is None:
        logger.error("テストケースのjsonの設定が正しくありません")
        exit(1)
    else:
        logger.info("target: " + str(target))
    
    # 時間計測
    import time
    time_s = time.time()
    ok_code = ""
    obj_rep = None
    gen_number = 0
    # 修正開始
    #try:
    ok_code, obj_rep, gen_number = main(input_Path, time_s,input_lang,target)
    #except Exception as e:
        #file = open(r"error_log.csv", "a")
        #file.write(str(datetime.datetime.now()) + ":" + str(input_Path) + ":" + str(e) + "\n")
        #file.close()
        #exit("490行目で終了しました")
    

    time_e = time.time()
    logger.info("All test passed")
    exe_time = time_e - time_s
    logger.info(exe_time)
    
    txt_time = cal_time(exe_time)
    logger.info("実行時間 " + txt_time)
    
    # 修正したコードをファイルに書き込む
    # logger.info(ok_code)
    # 修正したコードをファイルに書き込む
    f = open(output_Path, "w", encoding="UTF-8")
    f.write(ok_code)
    f.close()

    # 修正方法をファイルに書き込むE
    # 記録するデータ
    # data = ""
    # memo = ''
    res_datas = ['～'] * 9
    # 記録するパス
    csv_Path = json_data["csv_path"]            
    # 八百長
    # memo = "~"
    
    """if isEx:
        # memo = "自己参照"
        memo = "自己参照"  """   
    
    # 日付
    res_datas[0] = str(datetime.datetime.now())
    # 修正方法
    res_datas[1] = "WRONG"
    # 修正対象のパス
    res_datas[2] = input_Path
    # 世代数
    res_datas[3] = str(gen_number)
    # 修正時間
    res_datas[4] = str(exe_time)

    # 何もせずに修正に成功したとき
    if gen_number == -1:
        # 修正方法 
        res_datas[1] = "FIRST"
    # 修正に失敗したとき
    elif obj_rep is None:
        # 初期値から変更するところがありません！
        pass
        """# 日付
        data += 
        # 修正方法の記録
        data += "WRONG ,"
        # 修正対象のパス
        data += input_Path + ","
        # 世代数
        data += str(gen_number) + ","
        # 時間の記録
        data += str(exe_time)

        data += " ,"
        data += " ,"
        data += " ,"
        data += " ,"
        data += memo
        """
    # 修正に成功したとき
    else:
        # 修正方法の記録
        res_datas[1] = str(obj_rep.way)
        """# 修正対象のパス
        data += input_Path + ","
        # 世代数
        data += str(gen_number) + ","
        # 時間の記録
        data += str(exe_time) + ","
        """
        
        # 外部ソースコードのリスト
        ext_code_path = ""
        # 何かしら外部を使った場合
        if obj_rep.ext_id is not None:
            if len(external_codes) == 0:
                ext_code_path = "自己参照"
            else:  
                ext_code_path = str(external_codes[obj_rep.ext_id])
            res_datas[5] = ext_code_path
        
        # 修正した箇所のデータ
        # 削除したId
        res_datas[6] = str(obj_rep.del_num)
        # 挿入する親のId
        res_datas[7] = str(obj_rep.insert_parent)
        # 挿入する外部Id(文章)
        res_datas[8] = str(obj_rep.insert_id)
        # data += str(obj_rep.ext_id)     # 外部ソースコードのId(0から始まる)を引数に、
        # data += ","

    # if memo 

    # 記録ファイル
    record_txt = ",".join(res_datas)
    # 書き込み
    f = open(csv_Path, 'a', encoding="UTF-8")
    f.write(record_txt)
    f.write("\n")
    f.close()
    # exit()
        
def getUru_python():
    # python_uruのテスト
    WA_NUMS = 339
    # pythonのときのみコメントアウト
    # ex_sets = set(list((range(33,51))))
    # wa_codes = list(ex_sets)
    ex_sets = set()
    wa_codes = set()
    for i in range(WA_NUMS):        
        if i not in ex_sets:
            wa_codes.add(i)
    return wa_codes

def getUru_java():
    # java_uruのテスト
    WA_NUMS = 74
    ex_sets = set()
    wa_codes = set()
    for i in range(WA_NUMS):        
        if i not in ex_sets:
            wa_codes.add(i)        
    wa_codes.add(999)
    wa_codes.add(998)

    # GregorianCalendarが使われているやつ
    """
    wa_codes.remove(0)
    wa_codes.remove(2)
    wa_codes.remove(5)
    wa_codes.remove(7)
    wa_codes.remove(15)
    wa_codes.remove(16)
    wa_codes.remove(19)
    wa_codes.remove(32)
    wa_codes.remove(33)
    wa_codes.remove(34)
    wa_codes.remove(35)
    wa_codes.remove(36)
    wa_codes.remove(37)
    wa_codes.remove(68)
    wa_codes.remove(69)
    wa_codes.remove(70)
    wa_codes.remove(71)
    wa_codes.remove(72)
    wa_codes.remove(73)
    wa_codes.remove(122)
    wa_codes.remove(123)
    wa_codes.remove(124)
    wa_codes.remove(125)
    wa_codes.remove(126)
    wa_codes.remove(127)"""
    # 新しいjavaWAuruに対して、
    # Calenderが使われているやつ
    wa_codes.remove(19)
    wa_codes.remove(20)
    return wa_codes

def all_repair(times, list_inputNums):
    for time_N in range(times):
        for num in list_inputNums:
            # 八百長(ファイル指定)
            str_num = str(num).zfill(3)
            # 入力パス
            # 八百長 python
            ip = "uruPyWA/WA{}.py".format(str_num)
            op = "out_Result/20230116/WA{}.py".format(str_num + "_" + str(time_N))        
            # 八百長 java
            # input_Path = "uruJavaWA/WA{}.java".format(str_num)
            # output_Path = "out_Result/20230116/WA{}.java".format(str_num + "_" + str(time_N))
            # 出力パス
            rep_Main(ip,op)

if __name__ == "__main__":
    path_logger = 'log_config.json'
    path_set = 'settingsR.json'
    logger = setting_logFile(path_logger)
    # 修正に関する設定ファイルの読み込み
    json_file = open(path_set, 'r', encoding="UTF-8")
    json_data = json.load(json_file)
    test_p_num = json_data["test_p_num"]
    test_n_num = json_data["test_n_num"]
    test_p_case = json_data["test_p_case"]
    test_n_case = json_data["test_n_case"]
    test_p_score = json_data["test_p_score"]
    test_n_score = json_data["test_n_score"]
    external_codes = json_data["external_codes"]
    max_gen = json_data["max_gen"]
    memo = json_data["memo"]
    times = json_data["times"]
    # 修正対象のコードのパス
    input_Path = json_data["target_code"]
    # 出力するパス
    output_Path = json_data["output_code"]
    # データセットの取得
    wa_codes = getUru_python()
    # wa_codes = getUru_java()
    # データセットの変換
    list_inputNums = list(wa_codes)

    # 外部を使うか使わないか
    isEx = False

    #　総当たりの時
    # all_repair(times, list_inputNums)
    # ファイルを指定して実行するとき(jsonファイル)
    rep_Main(input_Path,output_Path)
    
    # すべて終わったら
    # 実験結果をメールで送信します。
    import Send_Mail
    Send_Mail.send_csv()

    #else:
    #    print(i, "は除外")