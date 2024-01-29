# coding: utf-8
y = int(input())

# ‰[”N”»’è
def isLeapYear(x_y):
    return "YES" if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0) else "NO"

print(isLeapYear(y))
