# Brute force method which has the time complexity of O(n log n + m log m) and space complexity of O(n+m)
def anagraam(a,b): 
    w=0
    for i in range(len(a)):
        if(a[i].isspace()==False):
            a[w]=a[i]
            w+=1
    a=''.join(a[0:w])
    w=0
    for i in range(len(b)):
        if(b[i].isspace()==False):
            b[w]=b[i]
            w+=1
    b=''.join(b[0:w])
    a.sort()
    b.sort()
    if(len(a)==len(b)):
        for i in range(len(a)):
               if(a[i]!=b[i]): 
                   return False
    else: 
         return False
    return True

# Optimized using Hash/Frequency mapping method to count frequency using dictonary which has the time complexity of O(n+m) and space complexity of O(k)
def optimized(a,c):
    for i in a:
        if(not i.isspace()):
           if(i not in c):
               c.update({i:1})
           else:
               c[i]+=1
    return c

a=input("Enter the String A :")
b=input("Enter the String B :")
c,d={},{}
c,d={},{}
e=anagraam(list(a),list(b))
print(f"Brute Force : {e} anagram")
c=optimized(a,c)
d=optimized(b,d)
if(c==d):
    print("Optimized Method : yes, It is a anagram")
else:
    print("Optimized Method : NO, it is not a anagram")