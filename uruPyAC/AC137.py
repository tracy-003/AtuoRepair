'''
s=input()
a= list(map(int, input().split()))
n = int(input())
n=5
a= [int(input()) for _ in range(n)]
k = int(input())
m=1000000007
from collections import defaultdict
d = defaultdict(int)
from collections import deque
print(' '.join(map(str,d)))
'''


n = int(input())
if n%400==0:
  print('YES')
elif n%100==0:
  print('NO')
elif n%4==0:
  print('YES')
else:
  print('NO')