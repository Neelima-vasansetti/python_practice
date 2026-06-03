def mergeSort(l,st,end):
    if st==end:
        return
    mid=(st+end)//2
    mergeSort(l,st,mid)
    mergeSort(l,mid+1,end)
    i=st
    j=mid+1
    l2=[]
    while i<=mid and j<=end:
        if l[i]<=l[j]:
            l2.append(l[i])
            i+=1
        else:
            l2.append(l[j])
            j+=1
    if i>mid:
        while j<=end:
            l2.append(l[j])
            j+=1
    elif j>end:
        while i<=mid:
            l2.append(l[i])
            i+=1
    for i in range(st,end+1):
        l[i]=l2.pop(0)
l=[2,8,1,4,9,8,2,6]
mergeSort(l,0,len(l)-1)
print(l)