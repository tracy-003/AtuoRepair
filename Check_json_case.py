def check(test_p_num,test_n_num
          ,test_p_case, test_n_case
          , test_p_score, test_n_score):
    checkList = []
    # ポジティブケースの個数と引数は同じかどうか
    print(type(len(test_p_case)), type(test_p_num))
    print(len(test_n_case), test_n_num)
    checkList.append((len(test_p_case)) == test_p_num)
    # ネガティブケースの個数と引数は同じかどうか
    checkList.append((len(test_n_case)) == test_n_num)
    
    if all(checkList):
        score = test_p_num * test_p_score + test_n_num * test_n_score
        return score
    
    # 同じでなければNoneを返す
    else:
        return None