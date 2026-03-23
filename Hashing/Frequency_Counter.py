# Frequency counter for numbers by using hash mapping which has the time complexity of O(n) and space commplexity of O(U) where U stands for unique values of list.
def frequency_counter(a): 
    for i in a:
        if(i not in count):
            count[i]=1
        else :
            count[i]+=1
    return count

count={}
a=list(map(int,input("Enter the array elements:").split()))
count=frequency_counter(a)
print(count)
