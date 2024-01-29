
# isf = True

def return_num(num):
    nums = [0,+1,-1,+1,-1]
    r = nums[num]
    """if isf and r < 0:
        r -= 1
        isf = False
        #exit()
    """
    return r


def return_end(num):
    #print("num", num)
    if num > 0:
        return "\n"
    else:
        return "\n"

def show(s):
    br = ["", "(", ")", "[", "]"]
    # s = input()
    s = "0" + s
    s = s.replace("(", "br@CKe2s1")
    s = s.replace(")", "br@CKe2s2")
    s = s.replace("[", "br@CKe2s3")
    s = s.replace("]", "br@CKe2s4")
    li = s.split("br@CKe2s")

    # print(li)

    # li.pop()

    indent_num = 0
    code = ""
    be = 10

    # indent = ""

    # print(li)
    # exit()

    # print(li)
    num = len(li)
    inL = [0] * num
    for i in range(num):
        l = li[i]
        code = ""
        # print(l)
        num = int(l[0])
        sent = br[num] + l[1:]
        code += sent
        # print(sent)
        # exit()
        """if num == be + 1:
            pass
        else:
            code += "\n"
        """    
        # code += "\n"
        
        
        # print(indent_num, code, end = "")
        # 番号を保持する
        be = num
        
        re = return_num(num)
        indent_num = indent_num + re
        # print("indent_num", indent_num)
        # print(indent_num)
        # exit()
        
        # 開業してからインデントする
        if re < 0:
            # indent_num1 += 1
            inL[i] = (indent_num + 1)
        else:
            inL[i] = indent_num
        
        li[i] = code 
        # indent = "\t" * indent_num1
        
        # print(indent_num1, code)
        
        # code += indent
        
    show1 = ""
    for c,i in zip(li,inL):
        # print(i,c)
        show1 += ("\t" * i)
        show1 += c
        show1 += "\n"

    return show1


