# Factorial by recursion method which has the time complexity of O(n) and space complexity of O(n)
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

num=int(input("Enter the number :"))
fact=factorial(num)
print("Factorial of the number is :",fact)