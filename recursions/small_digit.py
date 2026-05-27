def small(n):
  if n < 10:
    return n
  a = n % 10
  b = small(n // 10)
  if a < b:
    return a
  return b
print(small(51232))