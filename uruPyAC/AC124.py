import sys
input = sys.stdin.readline
def iinput(): return int(input())
def sinput(): return input().rstrip()
def i0input(): return int(input()) - 1
def linput(): return list(input().split())
def liinput(): return list(map(int, input().split()))
def miinput(): return map(int, input().split())
def li0input(): return list(map(lambda x: int(x) - 1, input().split()))
def mi0input(): return map(lambda x: int(x) - 1, input().split())
INF = 10**20
MOD = 1000000007

Y = iinput()
if Y % 400 == 0:
    print('YES')
elif Y % 100 == 0:
    print('NO')
elif Y % 4 == 0:
    print('YES')
else:
    print('NO')