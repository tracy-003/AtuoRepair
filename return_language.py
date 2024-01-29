import sys
def language_from_Path(path):
    # 拡張子を取得する
    kaku = kaku_from_Path(path)
    # 拡張子からプログラミング言語を判定する
    if kaku == "py":
        return "python"
    elif kaku == "java":
        return "java"
    
    else:
        # エラー出力
        sys.stderr.write("====================エラー出力====================\n")
        sys.stderr.write("言語が判定できませんでした。\n")
        sys.stderr.write(str(path) + "の拡張子 > " + str(kaku))
        exit(1)
        
def kaku_from_Path(path):
    # 拡張子を取得する
    kaku = path.split(".")[-1]
    return kaku