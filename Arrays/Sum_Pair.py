# Element by element search method which has time complexity of O(n^2)
def sum_pair(tar):
    pairs=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
           if (a[i]+a[j]==tar):
              pairs.append([a[i],a[j]])
    return pairs
                
# Using Single loop with effective search (Hash-set) which as time complexity of O(n)
def optimized(tar):
    visited=set()
    pair=[]
    for i in a:
        seen=tar-i
        if(seen in visited):
            pair.append([seen,i]) 
        visited.add(i)         
    return pair
     

a=[1,2,3,4,5]
p1,p2=[],[]
t=int(input("Enter the target element :"))
p1=sum_pair(t)
p2=optimized(t)
print ("Brute Force :",p1)
print("Optimized :",p2)