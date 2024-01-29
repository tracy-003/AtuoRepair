N = int(input())
if N % 400 == 0:
    print("YES")
elif N % 100 == 0:
    print("NO")
elif N % 4 == 0:
    print("YES")
else:
    print("NO")