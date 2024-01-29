Y = int(input())

if Y % 4:
  print('NO')
elif Y % 100 == 0 and Y % 400:
  print('NO')
else:
  print('YES')