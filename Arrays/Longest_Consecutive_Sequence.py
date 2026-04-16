# Longest Consecutive Sequence which has the time complexity of O(n log n) and space complexity of O(1)
def sequence_count(a):
    a.sort()
    count,max_count=1,1
    for i in range(1,len(a)):  
        if(a[i]==a[i-1]+1):
            count+=1
        else:
            if(count>max_count):
                max_count=count
            count=0 
    return max_count

a=[1,2,3,4,100,200]
print("Longest Consecutive count is : ",sequence_count(a))