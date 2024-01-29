Y = int(input())
Result = 'NO'
if Y%4==0:
  Result = 'YES'
if Y%100==0:
  Result = 'NO'
if Y%400==0:
  Result = 'YES'
print(Result)