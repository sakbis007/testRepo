class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

def insert_at_end(head,val):
    new_node=ListNode(val)
    if not head:
        return new_node
    current=head
    while current.next:
        current=current.next
    current.next=new_node
    return head

def build_list(values):
    head=None
    for value in values:
        head= insert_at_end(head,value)
    return head

def print_list(head):

    parts=[]
    current=head
    while current:
        parts.append(str(current.val))
        current=current.next
    print(" -> ".join(parts) + " -> None ")




# ---- Test It ----

list1 = build_list([1, 2, 4])
print_list(list1)

head_new=insert_at_end(list1, 1)
print_list(head_new)