Y = int(input())
if Y%4==0 and Y%400!=0:
    if Y%100==0:
        print('NO')
    else:
        print('YES')
elif Y%400==0:
    print('YES')
else:
    print('NO')