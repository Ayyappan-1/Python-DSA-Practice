# Max Heap Insertion which has the time complexity of O(log n) and space complexity of O(1). 
def max_heap_insertion(heap,element):
    heap.append(element)
    last_index=len(heap)-1

    while last_index>0: 
        current_parrent=(last_index-1)//2
        if(heap[current_parrent]< heap[last_index]):
            heap[current_parrent],heap[last_index]=heap[last_index],heap[current_parrent]
        else:
            break
        last_index=current_parrent
    return heap

heap=[5,4,3,2,1]
heap=max_heap_insertion(heap,6)
print(heap)