n,q=input().split()
n=int(n)
q=int(q)
l=[]
for i in range(n+1,q):
  if(i%2!=0):
    l.append(i)
print(*l)
