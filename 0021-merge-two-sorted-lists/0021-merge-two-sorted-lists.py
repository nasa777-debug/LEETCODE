# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return list1
        l=[]
        while list1:
            l.append(list1.val)
            list1=list1.next
        while list2:
            l.append(list2.val)
            list2=list2.next
        l.sort()
        l3=ListNode(l[0])
        temp=l3
        for i in range(1,len(l)):
            newnode=ListNode(l[i])
            temp.next=newnode
            temp=temp.next
        return l3