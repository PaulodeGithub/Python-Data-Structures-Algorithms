def find_middle_node(self):
    # 1. two pointers both starting at head
    slow = self.head
    fast = self .head

    #2.iterate as lonf as fast and fast.next are not None
    # error prevention
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    #3. slow is moving at half the speed of fast so will be half way 
    # when fast reaches the end of the list