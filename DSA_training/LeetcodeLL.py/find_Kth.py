def find_kth_from_end(ll, k):
    # 1. Initialize two pointers, 'slow' and 'fast', both pointing to the 
    # starting node of the linked list.
    slow = fast = ll.head   
    
    # 2. Move the 'fast' pointer 'k' positions ahead.
    for _ in range(k):
        # 2.1. If at any point during these 'k' movements, the 'fast' 
        # pointer reaches the end of the list, then it means the list 
        # has less than 'k' nodes, and thus, returning None is appropriate.
        if fast is None:
            return None
        
        # 2.2. Move the 'fast' pointer to the next node.
        fast = fast.next
 
    # 3. Now, move both 'slow' and 'fast' pointers one node at a time until 
    # the 'fast' pointer reaches the end of the list. Since the 'fast' pointer 
    # is already 'k' nodes ahead of the 'slow' pointer, by the time 'fast' 
    # reaches the end, 'slow' will be at the kth node from the end.
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. Return the 'slow' pointer, which is now pointing to the kth node 
    # from the end.
    return slow