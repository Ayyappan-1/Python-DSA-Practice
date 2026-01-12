def linear_search(a,target):
    for index,value in enumerate(a):
        if(target==a[index]):
            return index
    return -1
a=[1,2,3,6,9,12,56]
tar=int(input("Enter The Target Number :"))
index=linear_search(a,tar)
print("Not found....") if index==-1 else print(f"Found the Target at [{index+1}]")