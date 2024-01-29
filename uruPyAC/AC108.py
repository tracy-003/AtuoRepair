A = int(input())

x = A%4

if(A%400==0):print("YES")
elif(A%100==0):print("NO")

elif(x!=0):
    print("NO")
else:
    print("YES")
