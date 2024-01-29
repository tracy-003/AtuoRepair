Y = int(input())

if Y % 400 == 0:
    exit(print("YES"))
if Y % 100 == 0:
    exit(print("NO"))
if Y % 4 == 0:
    exit(print("YES"))
print("NO")