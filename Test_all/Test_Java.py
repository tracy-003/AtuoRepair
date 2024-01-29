import subprocess
import sys

import pathlib

def test(output_Path, test_in, test_out):
    # パスからファイル名を取得
    # 文字列
    Path_output_path = pathlib.Path(output_Path)
    name = Path_output_path.stem
    # コンパイル
    f_name = name + ".java"
    
    # print("name", name)
    # exit()


    # コンパイルエラーの時はFalseを返す
    try:
        con = subprocess.run(['javac', f_name])
    
    except Exception as e:
        print("Test_Java.py:javac:エラーが発生しました。", file=sys.stderr)
        print(e)
        return False
    #print("コンパイルを実行しました")
    
    # 実行
    # print("コンパイル：javac", f_name)
    # print("実行：java", name)
    #print(name, "を実行します")
    try:
        ans = subprocess.run(
            ['java', name]
            , input = str(test_in) + "\n"
            , encoding="utf-8"
            , capture_output = True
            , text = True # inputの確認
        )
    except subprocess.TimeoutExpired:
        # print error
        print("Timeout", file=sys.stderr)
        # exit()
        return False
    
    # print(ans.stdout)
    return str(ans.stdout) == str(test_out)

# import path
# output_Path = path.Path(r'C:\Users\user\new_study\trans\make_middle\testJava00.java')
# print(Test(output_Path, [2000, "YES\n"]))


