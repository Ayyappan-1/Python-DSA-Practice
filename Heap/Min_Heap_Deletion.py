# Min heap deletion which has the time complexity of O(log n) and space complexity of O(1)
def min_heap_delete(heap):
    if len(heap) == 0:
        return heap
    if len(heap) == 1:
        heap.pop()
        return heap
 
    heap[0] = heap[-1]
    heap.pop() 
    i = 0
    n = len(heap)
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
 
        if left < n and heap[left] < heap[smallest]:
            smallest = left 
        if right < n and heap[right] < heap[smallest]:
            smallest = right 
        if smallest == i:
            break 
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest

    return heap

heap=[1,2,3,4,5,6]
heap=min_heap_delete(heap)
print(heap)