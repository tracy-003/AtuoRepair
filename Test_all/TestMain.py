"""def test_python():
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
"""
# ここが呼び出される
from Test_all import Test_Java
from Test_all import Test_Python

def test(output_Path, test_case, input_lang):
    # 1.言語を判断する
    # 2.言語に応じてテストを実行する
    # 3.結果を返す
    
    # 入力値が複数になったら変える
    # test_in, test_out = test_case
    
    # 標準入力と標準出力を取得
    test_in, test_out = test_case
    test_out += "\n"
    
    if input_lang == "python":
        return Test_Python.test(output_Path, test_in, test_out)
    
    elif input_lang == "java":
        return Test_Java.test(output_Path, test_in, test_out)
    
    else:
        print("言語が非対応。テストできません")
        exit("TestMain.py:test")
    