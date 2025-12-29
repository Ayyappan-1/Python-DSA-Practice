# It just removes space and remains alphabets, numbers and symbols as it is... time coplexity is O(n^2) and space complexity O(n)
def space_removal(a,b):
    for i in a:
        if(i.isspace()):
            pass
        else:
            b+=i
    return b

# Optimized two pointer approach which has the time complexity of O(n) and space complexity of O(1)
def optimized(a):
    a=list(a)
    l=len(a)
    w=0
    for i in range(0,l):
        if(a[i].isspace()==False):
            a[w]=a[i]
            w+=1
    return ''.join(a[0:w])

b=''
a=input("Enter the string :")
b=space_removal(a,b)
print(b)

a=optimized(a)
print(a)