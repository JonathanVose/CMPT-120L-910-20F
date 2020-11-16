# List Comprehension

print([[x,y,z] for x in [1,2,3] for y in [4,5,6] for z in [7,8,9]])

# Coordinates where i + j + k do not = sum of x y and z

x = 1
y = 1
z = 1
n = 3

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) 
if i+j+k != n])