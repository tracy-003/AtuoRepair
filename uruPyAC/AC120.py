y=int(input())
u=False
if y%400==0:
  u=True
elif y%4==0 and y%100!=0:
  u=True
print("YES" if u else "NO")