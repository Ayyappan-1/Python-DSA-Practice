# Three varients of Sum Pair which has the time complexity of O(n) and space complexity of  O(n)

# Two sum which allows duplicates, all pairs 
def two_sum_all(a,target):
    visited=set()
    pair=[]
    for i in a: 
        needed=target-i
        if(needed in visited):
            pair.append([needed,i]) 
        visited.add(i) 
    return pair

# Two sum, Unique pairs only
def two_sum_unique(a,target):
    visited,pair=set(),set()
    for i in a: 
        needed=target-i
        if(needed in visited):
           if(needed<i):
                pair.add((needed,i)) 
           else:
                pair.add((i,needed))
        visited.add(i) 
    return pair

# Two sum, first pair (One pair)
def two_sum_single(a,target):
    visited=set() 
    for i in a: 
        needed=target-i
        if(needed in visited): 
            return [needed,i]
        visited.add(i) 
    return None


a=[1,2,3,4,4,2,3,5]
ap=two_sum_all(a,5)
up=two_sum_unique(a,5)
sp=two_sum_single(a,5)

print("All pairs :",ap)
print("Unique Pair :",list(map(list, up)))
print("Single Pair:",sp)