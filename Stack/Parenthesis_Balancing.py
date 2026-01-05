def parenthesis_balancing(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
 
        elif ch in mapping:
            if not stack:           
                return False

            top = stack.pop()
            if top != mapping[ch]:  
                return False
 
    return len(stack) == 0

a = "(){}()[(]"
result = parenthesis_balancing(a)
print("Parenthesis is well balanced") if result else print("Not balanced")
