class MinStack:
    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
            if not self.stack:
                return "Stack is empty"
            removed = self.stack.pop()
            if removed == self.min_stack[-1]:
                self.min_stack.pop()

            return removed
    def getMin(self):
            if not self.min_stack:
                return "Stack is empty"
            return self.min_stack[-1]

vault = MinStack()
vault.push(30)
vault.push(25)
vault.push(20)
vault.push(35)

print("Minimum temperature: ", vault.getMin())

vault.pop()

print("Minimum temperature after popping: ", vault.getMin())