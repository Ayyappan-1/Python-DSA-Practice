def majority_element():
    for i in range(len(a)):
        c=0
        for j in range(len(a)):
            if(a[i]==a[j]):
                c+=1
        if(c>len(a)//2):
            print(f"The majority Element is {a[i]} repeated {c}")
            return
        
    print("There is no majority element......")

a=[1,2,3,4,5,1,1,1,1]
majority_element()
