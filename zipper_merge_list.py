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


def merge_lists(list1, list2):
    vals=[]
    while list1:
        vals.append(list1.val)
        list1=list1.next
    while list2:
        vals.append(list2.val)
        list2=list2.next
    vals.sort()

    merged_list=build_list(vals)
    return merged_list


def merge_lists_optimized(list1,list2):
    dummy = ListNode(-1)
    current = dummy
    while list1 and list2:
        if list1.val<list2.val:
            current.next=list1
            list1=list1.next
        else:
            current.next=list2
            list2=list2.next
        current=current.next
    current.next=list1 if list1 else list2
    return dummy.next

def rev_list(head):
    current = head
    prev=None
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev
# ---- Test It ----

list1 = build_list([2,5,6,7])
print_list(list1)

# list2 = build_list([1, 2, 5])
# print_list(list1)
# merged_list= merge_lists(list1,list2)
# print_list(merged_list)

# merged_list_optimized = merge_lists_optimized(list1, list2)
# print("Merged List (Optimized):")
# print_list(merged_list_optimized)
rev_list=rev_list(list1)
print_list(rev_list)