# Subarray Sum Equals K by using hashing which has the time complexity of O(n) and space complexity O(n)
def subarray_sum_k(a, k):
    sum_count={0:1}
    count=sum=0
    for i in a:
        sum+=i
        previous=sum-k
        if(previous in sum_count):
            count+=sum_count[previous]
        if(sum in sum_count):
            sum_count[sum]+=1
        else:
            sum_count[sum]=1
    return count

print(subarray_sum_k([1,2,3,-3,3,4,5,3],3))