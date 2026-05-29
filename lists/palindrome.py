l = [1,2,2,1]
n = len(l)
count = 0
for i in range(0,n//2):
  if l[i] != l[n-1-i] :
    count = count+1
if count == 0:
    print("palindrome")
else :
    print("not palindrome")