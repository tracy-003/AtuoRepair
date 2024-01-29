y = int(input())
ans = 'NO'
if y % 400 == 0:
    ans = 'YES'
elif y % 100 == 0:
    ans = 'NO'
elif y % 4 == 0:
    ans = 'YES'
print(ans)