# ---- title -----
#https://atcoder.jp/contests/arc002/tasks/arc002_1
#A - ‚¤‚é‚¤”N
#2022-07-12
''' '''
# ---- program -----
n=int(input())

if(n%4==0):
  if (n%400!=0 and n%100==0):
    print("NO")
  else:
    print("YES")
else:
  print("NO")