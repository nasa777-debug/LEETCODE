# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        if head is None:
            return head
        while head:
            l.append(head.val)
            head=head.next
        i=0
        if len(l)%2!=0:
            for i in range(0,len(l)-1,2):
                l[i],l[i+1]=l[i+1],l[i]
        else:
            for i in range(0,len(l),2):
                l[i],l[i+1]=l[i+1],l[i]
        ans=ListNode(l[0])
        temp=ans
        for i in range(1,len(l)):
            temp.next=ListNode(l[i])
            temp=temp.next
        return ans