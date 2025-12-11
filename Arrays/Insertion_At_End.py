def insert(b):
   a.append(None)
   i=0
   while (a[i]!=None):
       i+=1
   a[i]=b

a=[1,2,3]
b=int(input("Enter the value to be inserted :"))
insert(b)
print(a)
