def evaluate_rpn(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a+b)
            elif token == "-":
                stack.append(a-b)
            elif token == "*":
                stack.append(a*b)
            elif token == "/":
                stack.append(int(a/b))
    return stack.pop()

expression = input("Enter RPN expression: ").split()
result = evaluate_rpn(expression)
print("Result:", result)