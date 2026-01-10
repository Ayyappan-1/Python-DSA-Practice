# Insertion Sort which has the Time complexity of O(n^2) and Space complexity of O(n)
def insertion_sort(a):
    n = len(a)
    for i in range(1, n): 
        key = a[i]
        pos = i

        for j in range(i - 1, -1, -1): 
            if a[j] > key:
                a[j + 1] = a[j]  
                pos = j
            else:
                break
        a[pos] = key  
    return a
 
a = [3, 4, 2, 1, 9, 0]
print(insertion_sort(a))
