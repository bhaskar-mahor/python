'''
Merge tow sorted list 
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
        # dummy head
        pos = dummyHead = Node(-1)
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                pos.next = list1
                list1 = list1.next
            else:
                pos.next = list2
                list2 = list2.next
            pos = pos.next
        # merge residual list1
        if list1 is not None:
            pos.next = list1
        # merge residual list2
        if list2 is not None:
            pos.next = list2
        return dummyHead.next

obj = Solution()
obj.mergeTwoLists()
