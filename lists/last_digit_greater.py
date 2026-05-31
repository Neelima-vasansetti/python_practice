a = [4,2,3,5,6,1]
n=len(a)
for i in range(0,n-1):
    if a[i]>a[i+1]:
        # i,i+1
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
print(a)