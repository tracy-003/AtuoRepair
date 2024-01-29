Y = int(input())
 
  
if Y % 4 != 0:
  print('No')
elif Y % 400 == 0:
  print("YES")
elif Y % 100 == 0:
  print('NO')
elif Y % 4 == 0:
  print('YES')