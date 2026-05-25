class ThemeParkQueue:
    def __init__(self):
        self.normal_queue = []
        self.vip_queue = []
    def add_normal(self, name):
        self.normal_queue.append(name)
        print(name, "joined normal queue")

    def add_vip(self, name):
        self.vip_queue.append(name)
        print(name, "joined VIP queue")

    def process_visitor(self):
        if len(self.vip_queue) != 0:
            visitor = self.vip_queue.pop(0)
            print(visitor, "processed from VIP queue")
        elif len(self.normal_queue) != 0:
            visitor = self.normal_queue.pop(0)
            print(visitor, "processed from normal queue")
        else:
            print("No visitors in queue")

    def display(self):
        print("VIP Queue:", self.vip_queue)
        print("Normal Queue:", self.normal_queue)
park = ThemeParkQueue()
park.add_normal("Alice")
park.add_normal("Bob")
park.add_vip("Charlie")
park.add_vip("Diana")
park.display()

print("\nProcessing visitors: \n")

park.process_visitor()
park.process_visitor()
park.process_visitor()

park.display()