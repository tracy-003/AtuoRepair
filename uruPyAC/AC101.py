y = int(input())
flg1 = False
flg2 = False
flg3 = False
if y%100==0:
    flg2 = True
if y%400==0:
    flg3 = True
if y%4==0:
    flg1 = True

if flg1 and flg2 and flg3:
    print('YES')
elif flg1 and flg2:
    print('NO')
elif flg2 and flg3:
    print('YES')
elif flg3 and flg1:
    print('YES')
elif flg1:
    print('YES')
elif flg2:
    print('NO')
elif flg3:
    print('YES')
else:
    print('NO')