'''
Given two sorted linked lists, merge them into one sorted linked list such that the resulting link list contains the original nodes two initial linked lists.

Input:
1->3->5
2->4

Output:
1->2->3->4->5


'''
# new head node
# point to smaller one
# save the
# set next to none


class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def merge_list(head1, head2):
    n_head = Node(0)
    curr_1 = head1
    curr_2 = head2
    res_head = n_head
    while curr_1 and curr_2:
        if curr_1.val > curr_2.val:
            temp = curr_2.next
            curr_2.next = None
            n_head.next = curr_2
            n_head = n_head.next
            curr_2 = temp
        else:
            temp = curr_1.next
            curr_1.next = None
            n_head.next = curr_1
            n_head = n_head.next
            curr_1 = temp

    if curr_1:
        n_head.next = curr_1
    if curr_2:
        n_head.next = curr_2

    return res_head.next


'''
Given two sorted linked lists, merge them into one sorted linked list such that the resulting link list contains the original nodes two initial linked lists.

Input:
1->3->5
2->4

Output:
1->2->3->4->5


'''
