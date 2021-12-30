'''
Given two sorted linked lists, merge them into one sorted linked list such that the resulting link list contains the original nodes from the two initial linked lists.

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
Given two unsorted linked lists, merge them into one sorted linked list such that the resulting link list contains the original nodes from the two initial linked lists. 
You may not use extra data structures (i.e. pylists (not linked lists), arrays, hashmaps, hashsets; NOTE: this is not the same as time complexity)

Input:
3->1->5
4->2

Output:
1->2->3->4->5

'''


def merge_sort(head1, head2):
    curr = head1
    while curr:
        curr = curr.next
    curr.next = head2

    def find_mid(head):
        fast_pointer = head
        slow_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

    # partitions
    def partition(head):
        if not head.next:
            return head

        mid = find_mid(head)
        curr = head
        while curr.next and curr.next != mid:
            curr = curr.next
        curr.next = None

        left = partition(head)
        right = partition(mid)

        n_head = merge_list(left, right)
        return n_head

    return partition(head1)


# find mid of LL
'''
O(n * log n)
| ------------------------- -> n
|            123456
|       123       456
|     12    3     45    6
|   1   2        4    5 - ---- log n
|     12     3     45     6
|      123         456
|            123456
V - ----- 2 log n
1
'''

'''
3->1->5 ->4->2

mid = 5
3->1-> 5
mid = 1
3->1
mid = 1
3

left = 3
1
right 1
1->3

5
mid = 5
1->3->5

4->2
mid 2
4

left = 4
right = 2
2->4

merge_list(1->3->5, 2->4)
1->2->3->4->5



'''
