# Brute Force which has the time complexity of O(n) and space complexity of O(n)
def array_reversal(a):
    b=[]
    for i in range(len(a)-1,-1,-1):
        b.append(a[i])
    return b

# Optimized method by using reversal algorithm which has the time complexity of O(n) and Space complexity of O(1)
def optimized(a):
    l=len(a)
    last_element=l-1
    for i in range(0,l//2):
        temp=a[i]
        a[i]=a[last_element]
        a[last_element]=temp
        last_element-=1 
    return a

a,b=[1,2,3,4,5,6,7,8],[]
b=array_reversal(a)
print("Brute Force : ",b)
a=optimized(a)
print("Optimized Method :",a)