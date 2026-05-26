def power(b,e):
    if e==0:
        return 1
    res = b*power(b,e-1)
    return res
print(power(2,8))