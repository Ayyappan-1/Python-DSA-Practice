# Assigning alternative signs in the array which has the time compelxity of O(n^2) and Space complexity of O(1)
def alternate(a):
    n = len(a)
    for i in range(n):
        if i % 2 == 0:        
            if a[i] < 0:

                for j in range(i+1, n):
                    if a[j] > 0:
                        a[i], a[j] = a[j], a[i]
                        break
        else:         
            if a[i] > 0:

                for j in range(i+1, n):
                    if a[j] < 0:
                        a[i], a[j] = a[j], a[i]
                        break
    return a 


# Optimized code uses two pointers which has the time compelxity of O(n) and Space complexity of O(1)
def optimized(a):
    minus=plus=i=0
    while len(a)>i: 
        while  plus<len(a) and a[plus]<0:
            plus+=1
        while  minus<len(a) and a[minus]>0:
            minus+=1  
            
        if(i%2==1):
            if(a[i]>0 and minus<len(a)):
                    a[i],a[minus]=a[minus],a[i] 
            i+=1

        else:
            if(a[i]<0 and plus<len(a)):
                    a[i],a[plus]=a[plus],a[i]
            i+=1
    return a 

a=  [-11, -12, 3, 4, 5]
print(f"Brute Force method : \n{alternate(a)}")
a=  [-11, -12, 3, 4, 5]
print(f"optimized method : \n{optimized(a)}")