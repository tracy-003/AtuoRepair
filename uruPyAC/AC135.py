def is_uruu(Y):
  if Y % 400 == 0:
    return True
  elif Y % 100 == 0:
    return False
  else:
    return Y % 4 == 0
D = {True:'YES', False:'NO'}
print(D[is_uruu(int(input()))])