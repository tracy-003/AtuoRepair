Y = int(input())

ans = 'No\n'

if (Y % 4 == 0) and (Y % 100 != 0):
  ans = 'Yes\n'
if (Y % 400 == 0) and (Y % 100 == 0):
  ans = 'Yes\n'
print(ans)