"""import sys



"�E�d�c���������E�d�c���������E�d�c��������"

read = sys.stdin.read

readline = sys.stdin.readline

"�E�d�c���������E�d�c���������E�d�c��������"





def main():

    Y = int(readline())



    ans = False



    if Y % 4 == 0:

        ans = True

    if Y % 100 == 0:

        ans = False

    if Y % 400 == 0:

        ans = True



    print("YES" if ans else "NO")





if __name__ == '__main__':

    INF = float('INF')

    MOD = 10 ** 9 + 7

    sys.setrecursionlimit(10 ** 5)

    "�E�d�c���������E�d�c���������E�d�c��������"

    main()

"""

Y = int(input())
ans = False
if Y % 4 == 0:
    ans = True
if Y % 100 == 0:
    ans = False
if Y % 400 == 0:
    ans = True

if ans:
    print("YES")
else:
    print("NO")