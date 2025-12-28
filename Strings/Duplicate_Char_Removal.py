# Brute force method which has the time complexity of O(n^2) and space compelxity of O(n)
def duplicate_character_removal(a): 
    b=''
    for i in a:
        if(i not in b):
            b+=i
    return b

# Optimized method uses hash set which has the time complexity of O(n) and Space complexity of O(n)
def optimized(a):
    b,w=set(),0
    for i in a:
        if (i not in b):
            b.add(i)
            a[w]=i
            w+=1
        else:
            pass
    return ''.join(a[0:w]) 

a="ayyasaaaayyyyy"
b=""
b=duplicate_character_removal(a)
print("Brute Force Method :",b)
a=optimized(list(a))
print("Optimized Method :",a)