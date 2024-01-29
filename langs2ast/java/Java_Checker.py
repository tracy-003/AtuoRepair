# 標準入力かどうかを判定する
def check(id):
    if "nextInt" in id:
        return (True, "int")
    else:
        return (False, None)