def minimum():
    min=a[0]
    for i in range(len(a)-1):
        if(min>a[i+1]):
            min=a[i+1]
    return min

a=[8,4,9,1]
min=minimum()
print(min)