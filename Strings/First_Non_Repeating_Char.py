# Brute Force apporach which has time complexity of O(n^2) and Space complexity of O(1)
def first_non_repearing_char(a):
    c=0
    l=len(a)
    for i in range(l):
        if(a[i].isspace()):
            continue
        for j in range(l):
            if(a[i]==a[j]):
                c+=1
        if(c==1):
            return a[i]
        c=0
    return False

# Optimized method using frequency dictionary method which has the time complexity of O(n) and space complexity of (k)
def optimized(a):
    c={}
    for i in a:
        if(not i.isspace()):
           if(i not in c):
               c.update({i:1})
           else:
               c[i]+=1 
    for i in a:
        if(c.get(i)==1):
            return i
    return False 

a="ayyaydfjdfhajkhfdjkhjhjkd 2342"
ans=first_non_repearing_char(a)
print("Brute Force :The string has no non repeating characters") if ans==False else print("Brute force :The first non repeating character is :",ans)
ans=optimized(a)
print("Optimized :The string has no non repeating characters") if ans==False else print("Optimized :The first non repeating character is :",ans)