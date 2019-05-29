n,k=input().split()
n=int(n)
k=int(k)
l=[]
for i in range(n+1,k):
  if(i>1):
    for t in range(2,i):
      if(i%t==0):
        break
    else:
        l.append(i)
print(*l)
