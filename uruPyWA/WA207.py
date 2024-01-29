year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("YES\n")
    else:
      print("NO\n")
  else:
    print("YES\n")
else:
  print("NO\n")