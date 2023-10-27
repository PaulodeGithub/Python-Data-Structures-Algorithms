class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1


    def reverse_between(self, start_index, end_index):
        # 1. Edge Case: If list has only one node or none, exit.
        if self.length <= 1:
            return
    
        # 2. Create a dummy node to simplify head operations.
        dummy_node = Node(0)
        dummy_node.next = self.head
    
        # 3. Init 'previous_node', pointing just before reverse starts.
        previous_node = dummy_node
    
        # 4. Move 'previous_node' to its position.
        # It'll be at index 'start_index - 1' after this loop.
        for i in range(start_index):
            previous_node = previous_node.next
    
        # 5. Init 'current_node' at 'start_index', start of reversal.
        current_node = previous_node.next
    
        # 6. Begin reversal:
        # Loop reverses nodes between 'start_index' and 'end_index'.
        for i in range(end_index - start_index):
            # 6.1. 'node_to_move' is next node we want to reverse.
            node_to_move = current_node.next
    
            # 6.2. Disconnect 'node_to_move', point 'current_node' after it.
            current_node.next = node_to_move.next
    
            # 6.3. Insert 'node_to_move' at new position after 'previous_node'.
            node_to_move.next = previous_node.next
    
            # 6.4. Link 'previous_node' to 'node_to_move'.
            previous_node.next = node_to_move
    
        # 7. Update list head if 'start_index' was 0.
        self.head = dummy_node.next
