def detectCycle(head):
    slow,fast = head,head

    if head and not head.next:
        return None
        
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            break

    if slow!=fast:
        return None
    
    fast = head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    
    return slow