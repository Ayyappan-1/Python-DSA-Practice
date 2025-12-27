# Brute Force which has the time compelxity of O(n^2) and Space complexity of O(1)
def majority_element(a):
    for i in range(len(a)):
        c=0
        for j in range(len(a)):
            if(a[i]==a[j]):
                c+=1
        if(c>len(a)//2):
            print(f"The majority Element is {a[i]} repeated {c}")
            return
        
    print("There is no majority element......")

# Optimized method (Boyer-Moore Voting Algorithm) which has the Time complexity of O(n) and Space complexity of O(1)
def optimized(a):
    c=0
    candidate=None
    for i in a:
        if(c==0):
            candidate=i
            c+=1
        elif(candidate==i):
            c+=1
        else:
            c-=1
    c=0
    for i in a:
        if(i==candidate):
            c+=1
    return candidate, c

a=[1,2,3,4,5,1,1,1,1]
majority_element(a)

candidate,c=optimized(a)
if(c>len(a)//2):
      print(f"The majority Element is {candidate}")
else:
    print("There is no majority element found.....")