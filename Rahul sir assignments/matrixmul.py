a=[[2,1],
   [3,4],
   [5,6]]
b=[[1,3,6],
   [2,4,5]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(a)):
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            result[i][j]+=a[i][k]*b[k][j]

for r in a:
    print(r)
for r in b:
    print(r)
for r in result:
    print(r)
