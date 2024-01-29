y = int(input())
ans = 'No'
if y % 400 == 0:
  print('Yes')
  exit()
if y % 100 == 0:
  print('No')
  exit()
if y % 4 == 0:
  ans = 'Yes'
print(ans)