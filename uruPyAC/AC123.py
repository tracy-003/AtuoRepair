Y = int(input())
if Y%400==0 or (Y%100!=0 and Y%4==0):
  print("YES")
else:
  print("NO")