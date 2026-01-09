# Bubble sort which has the time complexity of O(n^2) and time complexity O(n)

def bubble_sort(a):
    l=len(a)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(a)

a=[6,4,3,9,10]
bubble_sort(a)