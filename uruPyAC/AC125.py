y=int(input())
r="NO"
if y%4==0: r="YES"
if y%100==0: r="NO"
if y%400==0: r="YES"
print(r)