l = [8,3,5,7,10,9,1] #bubble sort
n = len(l)
for j in range(n-1):
 for i in range(0,n-1):
   if l[i] > l[i+1]:
      l[i+1],l[i] = l[i],l[i+1]
print(l)