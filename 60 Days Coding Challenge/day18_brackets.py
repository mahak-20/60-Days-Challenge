def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return False
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
        
    return len(stack) == 0

s = input("Enter bracket string: ")

if is_balanced(s):
    print("Valid")
else:
    print("Invalid")