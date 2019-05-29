a,b=input().split()
a=int(a)
b=int(b)
for i in range(a,b):
  count=0
  x=len(str(i))
  temp = i
  while(temp> 0):
   digit = temp % 10
   count += digit ** int(x)
   temp //= 10
  if(i==count):
   print(i,end="")
