def reverse(s):
  str=""
  for i in s:
    str=i+str
  return str
s=str(input("enter the name "))
print(s)
print(reverse (s))
