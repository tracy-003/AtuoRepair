n=int(input())
print('YES' if ((n%4==0)^(n%100==0)^(n%400==0)) else 'NO')