def insert(pos, b):
    global a
    l=len(a)
    a.append(None)
    for i in range(l-1,pos-1,-1):
        a[i+1]=a[i]
         
    a[pos]=b
        
a=[1,2,3,4,5]
b=3.4
pos=5
insert(pos-1,b)
print(a)
 
        