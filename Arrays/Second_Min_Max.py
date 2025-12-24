# Brute force method for sorting the array and fixing that b[1] is second smallest number and a[n-2] is the seond largest number
def unique_sorted_array(a):
    c,d=set(),[]
    l=len(a)
    for i in range(0,l):
        if(a[i] not in c):
            c.add(a[i])
            d.append(a[i])
    d=sorted(d) 
    return d

# Optimized method, single pass min-max tracking algorithm which has O(n)
def optimized(a):
    small, second_small, large, second_large =float('inf'),float('inf'), float('-inf'),float('-inf')
    for i in a:
        if(i<small):
            second_small=small
            small=i
        elif(i>small and i<second_small):
            second_small=i

        if(i>large):
            second_large=large
            large=i
        elif(i<large and i>second_large):
            second_large=i 
    
    return second_small,second_large

a=[0,0,0]
d=[]

d=unique_sorted_array(a)
if(len(d)<2):
        print("Can't evaluate, number of unique elements shoud be higher then 2") 

second_min,second_max=optimized(a)
if(second_min == float('inf') or second_max == float('-inf')):
        print("can't evaluate, number of unique elements shoud be higher then 2")
else:
        print(f"Optimized Method\nThe second smallest number is :{second_min}\nThe seond largest number is :{second_max}")
