def f1(a):
  if a>5:
    return
  f1(a+1)
  print(a)
f1(1)