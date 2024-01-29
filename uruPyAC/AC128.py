YNEOS=lambda conditions:print('YES' if conditions else 'NO')
YNeos=lambda conditions:print('Yes' if conditions else 'No')
S=lambda:input().split()
M=lambda:map(int,input().split())
L=lambda:list(map(int,input().split()))
O=lambda:map(int,open(0).read().split())
# split‚ğÁ‚·‚Æˆê•¶š‚¸‚Â
#########################################
y=int(input())
YNEOS((y%4==0 and y%100!=0) or y%400==0)
