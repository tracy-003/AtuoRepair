Y = int(input())
Result = ''
if Y%400==0:
  Result = 'YES'
elif Y%100==0:
  Result = 'NO'
elif Y%4==0:
  Result = 'YES'
else:
  Result = 'NO'
print(Result)