x=int(input())
y=list(map(int,input().split()))[:x]
for i in range(0,x):
  print(y[i],i)
