n=int(input())
if n%4>0: ans='NO'
elif n%400==0: ans='YES'
elif n%100==0: ans='NO'
else: ans='YES'
print(ans)