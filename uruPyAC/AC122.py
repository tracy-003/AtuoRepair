Y = int(input())

flag = False
if Y % 4 == 0:
    flag = True
    if Y % 100 == 0:
        flag = False
        if Y % 400 == 0:
            flag = True

print('YES' if flag else 'NO')