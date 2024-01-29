N = int(input())

ans = "NO"

if N % 4 == 0:

    if N % 100 == 0:

        if N % 400 == 0:

            ans = "YES"

        else:

            ans = "NO"

        ans = "NO"

    else:

        ans = "YES"

print(ans)

