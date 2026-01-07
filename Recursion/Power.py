# Power by recursion method which has the time complexity of O(b) and space complexity of O(b)
def power(a,b):
    if(b==0):
        return 1
    return a*power(a,b-1)

a=int(input("Enter A :"))
b=int(input("Enter B :"))
print(power(a,b))