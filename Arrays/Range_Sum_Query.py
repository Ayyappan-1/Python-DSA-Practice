# Brute force method for RSQ which has a insufficiency of (N x Q), increases time complexity for each range query.
def range_sum_query(l,r,a):
    s=0
    for i in range(l,r):
        s+=a[i]
    return s

# Optimization is done by using prefix sum algorithm which results in the operational time of O(1) and one time processing time of O(n)
def optimized(l,r,a):
    if(l==0):
       s=b[r]
    else:
       s=b[r]-b[l-1]
    return s
    

a=[1,2,3,4,5,6,7]
l=int(input("Enter the Starting Index :"))
r=int(input("Enter the Ending  Index :"))
s,length=0,0
b=[]
for i in a:
    s+=i
    b.append(s) 
    length+=1
    
if ( 0<l<length and 0<r<length):
   s=range_sum_query(l-1,r,a)
   print("Brute Force :",s)
   s=optimized(l-1,r-1,a)
   print("Optimized :",s)
else:
    print("Input is invalid, the numbers ranges above zero.........")