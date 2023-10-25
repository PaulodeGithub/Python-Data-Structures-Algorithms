def remove_duplicates(self):
    # 1. Initialize a set called 'values' to store unique node values.
    values = set()
    
    # 2. Initialize 'previous' to None. 
    # This will point to the last node we've seen that had a unique value.
    previous = None
    
    # 3. Start at the head of the linked list.
    current = self.head
 
    # 4. Traverse through the linked list.
    while current:
        # 4.1. Check if the value of the current node is already in the set.
        if current.value in values:
            # 4.1.1. If yes, bypass this node by pointing the next of 
            # 'previous' to the next of 'current'.
            previous.next = current.next
            
            # 4.1.2. Decrement the length of the list.
            self.length -= 1
        else:
            # 4.2. If not, add the value to the set.
            values.add(current.value)
            
            # 4.2.1. Update the 'previous' to point to 'current' now.
            previous = current
 
        # 4.3. Move to the next node in the list.
        current = current.next
