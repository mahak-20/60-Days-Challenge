def is_valid(expression):
    stack = []
    for ch in expression:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if len(stack) == 0:
                return False
            top = stack[-1]
            if ch == ')' and top == '(':
                stack.pop()
            elif ch == '}' and top == '{':
                stack.pop()
            elif ch == ']' and top == '[':
                stack.pop()
            else:
                return False
            
    if len(stack) != 0:
        return False
    return True
    
expression = input("Enter brackets: ")
if is_valid(expression):
    print("Balanced")
else:
    print("Not Balanced")
