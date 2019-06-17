n,m = input().split()
k = 0
for i in range(len(n)) :
    if n[i] != m[i] :
        k += 1
if k == 1 : 
  print('yes')
else :      
  print('no')
