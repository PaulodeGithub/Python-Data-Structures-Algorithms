class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent_index(self, index):
        return (index -1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current > 0 and self.heap[current] > self.heap[self.parent_index(current)]:
            self.swap(current, self.parent_index(current))
            current = self.parent_index(current)
    
    def sink_down(self, index):
        max_index = index

        while True:
            left_index = self.left_child(index)
            right_index = self.right_child_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = left_index
            
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value