




class Node():
    def __init__(self,val,next=None):
        self.value=val
        self.next=next

class Link():
    def __init__(self):
        pass

    def Link_Node(self,lis):
        if len(lis)==0:
            return
        dummy=head=Node(0)
        for i in lis:
            head.next=Node(i)
            head=head.next
        return dummy.next

    def reverse(self,head):
        previous=None
        current=head
        while current:
            t=current.next
            current.next=previous
            previous=current
            current=t
        return previous.next

    # def delete(self,head,target):
    #     dummy=Node(0)
    #     current=dummy
    #     while head:
    #         if head.value!=target:
    #             current.next=Node(head.value)
    #             current=current.next
    #         head = head.next
    #     return dummy.next
    def delete_1(self,head,target):
        current= dummy=Node(0)
        dummy.next=head
        current.next=head
        while current.next:
            if current.next.value!=target:
                current.next=current.next.next
            current = current.next
        return dummy.next


a=Link()
head=a.Link_Node([1,2,3,4,5])
a.delete(head,2)