#A - ‚¤‚é‚¤”N
Y = int(input())
if Y % 400 == 0:
    ans = "YES"
elif Y % 100 == 0:
    ans = "NO"
elif Y % 4 == 0:
    ans = "YES"
else:
    ans = "NO"

print(ans)