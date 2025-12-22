# Brute force method to find Subarray Max Sum 
def subarray(a):
    l=len(a)
    b=[]
    for i in range(l):
        s=0
        for j in range(i,l):
               s+=a[j]
               b.append(s) 
    return max(b)

# Optimized method (Kadane's Alogrithm)
def optimized(a):
     max_sum,current_sum=a[0],0
     for i in a:
          current_sum+=i
          if(current_sum<a[i]):
               current_sum=0
          if(current_sum>max_sum):
               max_sum=current_sum
     return max_sum

a=[1,2,-8,9,3]
max_sum=subarray(a)
print("Brute Force Method :",max_sum)
max_sum=optimized(a)
print("Optimized Method :",max_sum)