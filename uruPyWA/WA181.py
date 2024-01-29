Y = int(input())

flg = False
if Y % 400:
  flg = True
elif Y % 100:
  flg = False
elif Y % 4:
  flg = True
else:
  flg = False
  
print("YES" if flg else "NO")