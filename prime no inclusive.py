l, r = map(int,input().split())
count = 0
for i in range(l,r+1):
    for j in range(2,i):
      if i % j == 0:
        break
    else:
      count += 1
print (count)l, r = map(int,input().split())
count = 0
for i in range(l,r+1):
    for j in range(2,i):
      if i % j == 0:
        break
    else:
      count += 1
print (count)
