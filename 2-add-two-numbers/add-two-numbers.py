# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        b=[]
        while l1:
            a.append(l1.val)
            l1=l1.next
        while l2:
            b.append(l2.val)
            l2=l2.next
        i=int(''.join(map(str,a[::-1])))
        j=int(''.join(map(str,b[::-1])))
        k=i+j
        k=str(k)
        h=k[::-1]
        ans = None

        for x in h[::-1]:
            new = ListNode(int(x))
            new.next = ans
            ans = new

        return ans