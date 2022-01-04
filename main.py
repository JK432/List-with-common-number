# Write a Python Function that takes two lists and returns True if they have at least one common memebr
def fun(l,j):
  for x in l:
    if x in j:
      print(x)
h=[]
        
k=[]


j=input()
h=j.split()

g=input()
k=g.split()


fun(h,k)
