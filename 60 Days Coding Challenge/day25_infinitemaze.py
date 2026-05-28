class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = b

print("Maze 1 has cycle:", detect_cycle(a))  
x = Node(10)
y = Node(20)
z = Node(30)

x.next = y
y.next = z
print("Maze 2 has cycle:", detect_cycle(x))