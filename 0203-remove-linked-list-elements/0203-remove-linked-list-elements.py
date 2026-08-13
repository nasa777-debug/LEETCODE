# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        l=[]
        if head is None:
            return head
        while head:
            l.append(head.val)
            head=head.next
        l1=[i for i in l if i!=val]
        if l1==[]:
            return head
        r=ListNode(l1[0])
        temp=r
        for i in range(1,len(l1)):
            temp.next=ListNode(l1[i])
            temp=temp.next
        return r