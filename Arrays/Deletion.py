def delete(pos):
    global a
    l=len(a)-1
    for i in range(pos-1,l,1):
        a[i]=a[i+1]
    a[l]=None


a=[1,2,3,4,5,6]
print("The elements of Array :")
for pos,ele in enumerate(a):
    print(f"Position {pos+1} : Value {ele}")
   
position=int(input("Enter the position to delete :"))
delete(position)
print(a)
