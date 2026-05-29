class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print("None")

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    slow = dummy
    fast = dummy

    for i in range(n + 1):
        fast = fast.next
        
    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next

a = Node("Msg1")
b = Node("Msg2")
c = Node("Msg3")
d = Node("Msg4")
e = Node("Msg5")

a.next = b
b.next = c
c.next = d
d.next = e

print("Original msg chain:")
print_list(a)

head = remove_nth_from_end(a, 2)

print("Updated msg chain: ")
print_list(head)