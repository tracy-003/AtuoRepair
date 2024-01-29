# ブロックにした後に、もう一度同じ言語に戻せるかの確認です。# pythonの場合は、astにしてから
import make_Block
from ast2langs import ast2lang

def write_record(bl,co, num):
    file = open(r"C:\Users\user\new_study\trans\make_middle\res_ret.txt", "a")
    """if type(bl) is str:
        file.writelines("makeブロックにできませんでした\n")
        file.writelines(bl)
        file.write("\n")
    else:
        file.writelines(bl.print_Block(True))
        file.write("\n")
        file.writelines(str(co))
        file.write("\n")
    file.writelines("======================================================================================================\n")
    """
    file.writelines(str(num).zfill(3) + "," +  bl + "," +  co + "\n")

    file.close()

def ret(lo,ip, num):
    print(ip,"をRetranceします！")
    # ブロックにする。
    test_block = None
    code = ""
    try:
        test_block = make_Block.main(lo,ip)
        print("ブロックの表示")
    except Exception as e:
        test_block = str(e)
        # write_record(test_block, code)
        print("エラー：ブロックにできませんでした。Test_Retrance.py")
        print(str(e))
        import traceback
        traceback.print_exc()
        write_record(str(None), "yet!", str(num))
        return
    
    print("♪" * 30)
    test_block.print_Block(True)
    print("♪" * 30)

    # exit("ブロック化まで終わりました")

    print("=" * 20, "再翻訳後のコード", "=" * 20)
    test_block_print = "OKEY"
    try:
        code = ast2lang.return_All_code(test_block)
        print("翻訳後に変換")
        print(code)
    except Exception as e:
    
        code = None
        # test_block = str(e)
        # code = "okey"
        write_record(test_block_print,"=NG=:An Error", str(num))
        print("エラー：再翻訳できませんでした。Test_Retrance.py")
        import traceback
        traceback.print_exc()
        return
    
    if code is None:
        # test_block = str(e)
        code = "~NG~:code is None"
        write_record(test_block_print,str(code), str(num))
        print("エラー：再翻訳でNoneが返却されました。Test_Retrance.py ")
        return
    
    print("再翻訳のコード表示")
    print("#" * 50)
    print(code)
    print("#" * 50)

    code = "okey"
    # test_block = "okey"
    write_record(test_block_print, code, str(num))

def main0():
    ex_set = set()
    ex_set.add(2) # 関数系
    ex_set.add(19) # カレンダーあり
    ex_set.add(20) # カレンダーあり
    ex_set.add(21)
    ex_set.add(22)
    ex_set.add(23)
    ex_set.add(24)
    ex_set.add(25)
    ex_set.add(26)
    ex_set.add(39)
    ex_set.add(40)
    ex_set.add(41)
    ex_set.add(42)
    ex_set.add(43)
    ex_set.add(44)
    ex_set.add(45)
    ex_set.add(46)
    ex_set.add(47)
    ex_set.add(48)
    ex_set.add(49)
    ex_set.add(50)
    ex_set.add(75)

    for i in range(75):
        if i in ex_set:
            s = str(i) + "番目のファイルにwhileが含まれているため、スキップします。\n"
            if i == 2:
                s = str(i) + "番目のファイルに関数系が含まれているため、スキップします。\n"

            file = open(r"C:\Users\user\new_study\trans\make_middle\res_ret.txt", "a")
            file.writelines(s)
            # file.write("======================================================================================================\n")
            file.close()
        else:
            input_path = r"C:\Users\user\new_study\trans\make_middle\uruJavaWA\WA{}.java".format(str(i).zfill(3))
            logger = ""
            ret(logger, input_path, i)

def main1(num):
    input_path = r"C:\Users\user\new_study\trans\make_middle\uruPyWa\WA{}.py".format(str(num).zfill(3))
    input_path = r"C:\Users\user\new_study\trans\make_middle\uruPyWa\WA{}.py".format(str(num).zfill(3))
    logger = ""
    ret(logger, input_path, num)

# 確認用
if __name__ == "__main__":
    main1(189)
    # main0()