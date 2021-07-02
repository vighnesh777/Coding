def booleanMatrix(matrix):
    # code here 
    d1={}
    l1=[]
    l2=[]
    d2={}
    m=matrix
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j]==1:
                d1[i]=i
                d2[j]=j
    for i in d1:
        l1.append(d1[i])
    for j in d2:
        l2.append(d2[j])
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i in l1 or j in l2:
                matrix[i][j]=1
#driver code
r,c=map(int,input().split())
m=[]
for i in range(r):
  m.append(list(map(int,input().split())))
booleanMatrix(m)
for i in range(r):
  for j in range(c):
    print(m[i][j])
  print()
  
