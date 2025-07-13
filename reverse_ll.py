class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self,head):
        self.head=head
    def print(self,head):
        curr=head
        while curr is not None:
            print(curr.val,end=" ")
            curr=curr.next
        
    def length(self,head):
        curr=head
        n=0
        while curr is not None:
            n+=1
            curr=curr.next
        return n
    def reverseList(self,head,m):
        if not head or m==1 or m==0:
            return head
        dummy=ListNode(0)
        dummy.next=head

        pre_seg=dummy
        seg_head=head
        prev=None
        curr=seg_head
        count=0
        while curr and count<m:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            count+=1
        pre_seg.next=prev
        seg_head.next=curr
        return dummy.next

    

head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)

L1=LinkedList(head)
L1.print(head)

new_head=L1.reverseList(L1.head,2)
L1.print(new_head)