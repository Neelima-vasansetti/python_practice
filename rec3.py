def f1(a,n):
  if a>50:
    return
  if a%2==0:
    print(a)
  f1(a+1,n)
f1(2,100)