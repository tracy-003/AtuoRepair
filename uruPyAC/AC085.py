n=int(input())
flag=0
if n%4==0:
  flag=1
if n%100==0:
  flag=0
if n%400==0:
  flag=1
print("YES" if flag else "NO")