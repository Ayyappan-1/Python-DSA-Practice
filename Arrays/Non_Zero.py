#Brute force Approach 
def non_zero():
    c=0
    for i in range(len(a)):
        if(a[i]==0):
            c+=1
        else:
            b.append(a[i])
    for i in range(c):
        b.append(0)
        
#Optimized Apporch using Two pointers
def Optimized():
    w=0
    for r in range(len(a)):
        if(a[r]!=0):
            a[w]=a[r]
            w+=1
    for i in range(w, len(a)):
        a[i]=0

a=[1,0,2,0,3,4]
b=[]
non_zero()
print("Brute Force Method :",b)
Optimized()
print("Optimized method :",a)
        