def partition_list(self, x):
    # 1. Edge case: Check if the list is empty. If so, exit.
    if not self.head:
        return None
 
    # 2. Create two dummy nodes: 
    # dummy1 for nodes with values less than x 
    # and dummy2 for nodes with values greater or equal to x.
    dummy1 = Node(0)
    dummy2 = Node(0)
 
    # 3. Initialize two pointers (prev1 and prev2) at the dummy nodes.
    # They will be used to build the two separate lists.
    prev1 = dummy1
    prev2 = dummy2
 
    # 4. Start iterating from the head of the original list.
    current = self.head
 
    # 5. Traverse the entire list.
    while current:
        # 5.1. If the current node's value is less than x:
        if current.value < x:
            # 5.1.1. Attach it to the end of the list starting at dummy1.
            prev1.next = current
            # 5.1.2. Move the prev1 pointer forward.
            prev1 = current
        # 5.2. Otherwise:
        else:
            # 5.2.1. Attach it to the end of the list starting at dummy2.
            prev2.next = current
            # 5.2.2. Move the prev2 pointer forward.
            prev2 = current
        
        # 5.3. Move to the next node in the original list.
        current = current.next
 
    # 6. End the two lists. Set the next pointers of prev1 and prev2 to None.
    prev1.next = None
    prev2.next = None
 
    # 7. Link the end of the first list (the one that started at dummy1) 
    # to the beginning of the second list (the one that started at dummy2).
    prev1.next = dummy2.next
 
    # 8. Update the head of the linked list to point to the beginning 
    # of the partitioned list.
    self.head = dummy1.next
