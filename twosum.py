'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

'''
from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        current=head
        carry=0

        while l1 is not None or l2 is not None or carry!=0:
            dig1=l1.val if l1 is not None else 0
            dig2=l2.val if l2 is not None else 0

            tsum=dig1+dig2+carry
            dig=tsum%10
            carry=tsum//10
            node=ListNode(dig)
            current.next=node
            current=current.next

            l1=l1.next if l1 is not None else None
            l2=l2.next if l2 is not None else None
        
        res=head.next
        head.next=None
        return res


        


                



