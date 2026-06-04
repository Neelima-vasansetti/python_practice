def Ref(l, idx, key):
    if idx == len(l):
        return 0

    if l[idx] == key:
        return 1 + Ref(l, idx + 1, key)

    return Ref(l, idx + 1, key)

l = [10, 20, 10, 30, 10]
a = Ref(l, 0, 10)
print(a)