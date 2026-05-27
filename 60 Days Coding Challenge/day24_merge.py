class Soldier:
    def __init__(self, data):
        self.data = data
        self.next = None

class ArmyList:
    def __init__(self):
        self.head = None
    def add_soldier(self, data):
        new_node = Soldier(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    def print_army(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ->")
            temp = temp.next
        print("None")
def merge_armies(head1, head2):

    dummy = Soldier(0)
    tail = dummy
    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1

    if head2:
        tail.next = head2
    return dummy.next

army1 = ArmyList()
army1.add_soldier(1)
army1.add_soldier(3)
army1.add_soldier(5)
army1.add_soldier(7)

army2 = ArmyList()
army2.add_soldier(2)
army2.add_soldier(4)
army2.add_soldier(6)
army2.add_soldier(8)
print("Army 1:")
army1.print_army()
print("Army 2:")
army2.print_army()
merged_head = merge_armies(army1.head, army2.head)
print("Merged Army:")
temp = merged_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")