# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        if head is None:
            return head
        while head:
            l.append(head.val)
            head=head.next
        l1=[]
        if len(l)%2==0:
            l1=l[(len(l)//2):]
        else:
            l1=l[len(l)//2:]
        ans=ListNode(l1[0])
        temp=ans
        for i in range(1,len(l1)):
            temp.next=ListNode(l1[i])
            temp=temp.next
        return ans