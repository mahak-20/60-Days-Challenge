class Carriage:
    def __init__(self, data):
        self.data = data
        self.next = None

class Train:
    def __init__(self):
        self.head = None

    def add_carriage(self, data):
        new_carriage = Carriage(data)
        if self.head is None:
            self.head = new_carriage
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_carriage

    def print_train(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    def reverse_train(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

train = Train()
train.add_carriage("Engine")
train.add_carriage("Carriage 1")
train.add_carriage("Carriage 2")
train.add_carriage("Carriage 3")

print("Original Train Order:")
train.print_train()

train.reverse_train()
print("Reversed Train Order:")
train.print_train()