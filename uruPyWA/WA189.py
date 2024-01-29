year = int(input())



if year % 4 == 0:

  if year % 100 == 0:

    if year % 400 == 0:

      print("Yes\n")

    else:

      print("No\n")

  else:

    print("Yes\n")

else:

  print("No\n")