a=int(input())
temp=a
count=0
while(temp>0):
  r=temp%10
  count += r**3
  temp//=10
if(a==count):
  print("yes")
else:
  print("no")
