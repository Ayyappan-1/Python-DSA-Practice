def prefix():
    su=0
    for i in range(len(a)):
        su+=a[i]
        pre.append(su)

pre=[] 
a=[ 2, 4, 6, 8]
prefix()
print(pre)