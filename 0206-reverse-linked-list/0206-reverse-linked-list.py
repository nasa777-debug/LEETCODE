# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        if head is None:
            return head
        x=0
        while head:
            a.append(head.val)
            x=head.val
            head=head.next
        l3=ListNode(x)
        temp=l3
        l=a[::-1]
        for i in range(1,len(l)):
            newnode=ListNode(l[i])
            temp.next=newnode
            temp=temp.next
        return l3     