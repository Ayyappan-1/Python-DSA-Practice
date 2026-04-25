# Max Heap Deletion which has the time complexity of O(log n) and space complexity of O(1)
def max_heap_deletion(heap):
    length=len(heap)
    if(length==0):
        return heap
    if(length==1):
        heap.pop()
        return heap
    heap[0]=heap[length-1]
    heap.pop()
    length-=1
    i=0
    while True:
        left=2*i+1
        right=2*i+2
        greatest=i
        if(left<length and heap[greatest]<heap[left]):
            greatest=left
        if(right<length and heap[greatest]< heap[right]):
            greatest=right
        if(greatest==i):
            break
        heap[greatest],heap[i]=heap[i],heap[greatest]
        i=greatest
    return heap

heap=[6,5,4,3,2,1]
heap=max_heap_deletion(heap)
print(heap)