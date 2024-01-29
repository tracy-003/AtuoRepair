Y = int(input())

ans = 'NO\n'

if (Y % 4 == 0) and (Y % 100 != 0):
  ans = 'YES\n'
if (Y % 400 == 0) and (Y % 100 == 0):
  ans = 'YES\n'
print(ans)