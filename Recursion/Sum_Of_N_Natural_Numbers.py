# Sum of n numbers by using recursion which has the time complexity of O(n) and space complexity of O(n)
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("Enter the number :"))
su=sum(n)
print("The sum of N number is :",su)