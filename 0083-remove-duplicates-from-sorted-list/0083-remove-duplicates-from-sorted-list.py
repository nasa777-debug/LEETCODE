# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        if head is None:
            return head
        while head:
            l.append(head.val)
            head=head.next
        s=set(l)
        l1=list(s)
        l1.sort()
        ans=ListNode(l1[0])
        temp=ans
        for i in range(1,len(l1)):
            temp.next=ListNode(l1[i])
            temp=temp.next
        return ans