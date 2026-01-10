# Selection Sort which has the Time complexity of O(n^2) and Space complexity of O(n)
def selection_sort(a):
    l=len(a)
    for i in range(l):
        min=i
        for j in range(i,l):
            if(a[min]>a[j]):
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
    print(a)

a=[6,5,4,9,0]
selection_sort(a)