# String reversal by recursion method which has the time complexity of O(n) and space complexity of O(n)
def string_reversal(a,i):
    if(i==0):
        return a[0] 
    return a[i]+string_reversal(a,i-1) 
    

a=input("Enter the string :")
b=string_reversal(a,len(a)-1)
print(b)
