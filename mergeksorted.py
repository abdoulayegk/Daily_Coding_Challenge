"""Given k sorted singly linked lists, write a function to merge all the lists
into one sorted singly linked list.
"""


class Solution(object):
    def mergeKLists(self, lists):
        root = ListNode(0)
        tmp = []
        for i in lists:
            while i:
                tmp.append(i.val)
                i =  i.next
        tmp.sort()
        p = root
        for i in range(len(tmp)):
            p.next = ListNode(tmp[i])
            p = p.next
        return root.next
