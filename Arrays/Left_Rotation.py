# Brute force method for left rotation
def left_rotation(a,d):
    l=len(a)-1
    for i in range(0,d):
        a.append(None) 
        a[l+1]=a[0]
        a.pop(0)
    print(a)

a=[1,2,3,4,5,6,7,8,9]
d=int(input("Enter Number of Rotation Needed :"))
left_rotation(a,d)