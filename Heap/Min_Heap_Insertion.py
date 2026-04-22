# Min heap insertion operation which has the time complexity of O(log n) and space complexity of O(1)
def min_heap_insertion(heap,element):
    heap.append(element)
    index=len(heap)-1 
    while index>0 :
        if(heap[index] < heap[(index-1)//2]):
            heap[(index-1)//2],heap[index]=heap[index], heap[(index-1)//2] 
        else :
            break
        index=(index-1)//2
    return heap

heap=[1,2,4]
heap=min_heap_insertion(heap,0)
print(heap)

