import linked_list

def merge_list(L1, L2):
    dummy = tail = ListNode()

    while L1 and L2:
            if L1.data < L2.data:
                tail.next = L1
                L1 = L1.next
            else:
                tail.next = L2
                L2 = L2.next

    tail.next = L1 or L2
    return dummy.next
