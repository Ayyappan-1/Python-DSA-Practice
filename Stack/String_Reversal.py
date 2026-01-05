# Palindrome by using stack which has the time complexity of O(n) and space complexity of O(n/2)
def palindrome(a): 
    stack=[]
    l,start=len(a),0
    for i in range(l//2):
        stack.append(a[i])
    start=l//2 if(l%2==0) else (l//2)+1
    for j in range(start,l):
        popped=stack.pop()
        if(a[j]!=popped):
            return False
    return True

a=input("Enter the sting :")
result=palindrome(a)
print("Yes, palindrome") if result else print("No, it is not a palindrome")