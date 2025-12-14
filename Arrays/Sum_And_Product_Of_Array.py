def Sum_Prod_Array():
    s,p=0,1
    for i in range(len(a)):
        s+=a[i]
        p*=a[i]
    return s,p

a=[1,2,3,4]
s,p=Sum_Prod_Array()
print(f"Sum of the Array :{s}\nProduct of the Array : {p}")