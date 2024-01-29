Y = int(input())
ans = 'NO'
if Y % 4 == 0:
    ans = 'YES'
if Y % 100 == 0:
    ans = 'NO'
if Y % 400 == 0:
    ans = 'YES'
print(ans)