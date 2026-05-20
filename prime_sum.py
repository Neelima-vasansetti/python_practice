n = int(input("enter a number: "))
sum = 0
for i in range(2,n+1):
  count = 0
  for j in range(1,i+1):
    if(i%j==0):
      count += 1
  if count==2:
    sum = sum+i
print(sum)