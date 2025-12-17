def sum_pair(tar):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
           if (a[i]+a[j]==tar):
              pairs.append([a[i],a[j]])
                
pairs=[]
a=[1,2,3,4,5]
t=int(input("Enter the target element :"))
sum_pair(t)
print (pairs)