num = [1,7,4,3,1,5,9,88,88,3]
m = []
for i in range(len(num)):
  if num[i] not in m:
    m.append(num[i])
print(m)