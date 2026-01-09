# Brute force for non alphabets removal which has the time complexity of O(n) and space complexity of O(n)
def remove_non_alpha(a):
    b=""
    for i in a:
        if(i.isalpha()):
            b+=i
    return b

# Optimized method by using two pointers which has the time complexity of O(n) and Space complexity of O(1)
def optimized(a):
    a=list(a)
    w=0
    for r in a:
        if(r.isalpha()):
            a[w]=r
            w+=1
    return ''.join(a[:w])


a=input("Enter the string :")
b=''

b=remove_non_alpha(a)
print("Brute Force :",b)

a=optimized(a)
print("Optimized Method :",a)

