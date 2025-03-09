x = int(input("enter an integer of x:"))
y = int(input("enter an integer of y:"))
z = int(input("enter an integer of z:"))
n = int(input("enter an integer of n:"))
result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
print(result)