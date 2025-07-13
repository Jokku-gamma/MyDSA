class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def print_list(self, head):
        curr = head
        values = []
        while curr is not None:
            values.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(values) + " -> None")

    def length(self, head):
        curr = head
        n = 0
        while curr is not None:
            n += 1
            curr = curr.next
        return n
    def reverseN(self,head,x,y):
        if not head or x>=y:
            return head
        temp=head
        i=0
        while i<x:
            temp=temp.next
        dummy=ListNode(0)
        dummy.next=temp
        pre_seq=dummy
        seq_head=temp
        prev=None
        curr=seq_head
        while x<y:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            x+=1
        pre_seq.next=prev
        seq_head.next=curr
        return dummy.next
    
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
ll1 = LinkedList(head1)
print("Original list:")
ll1.print_list(ll1.head) 

new_head1=ll1.reverseN(ll1.head,1,4)
ll1.print_list(new_head1)