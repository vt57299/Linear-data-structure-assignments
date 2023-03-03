# Q6. Write a program to convert prefix expression to infix expression.

def is_operator(a):
    if a == "+" or a == "-" or a=="/" or a == "*" or a == ")" or a == "(" or a == "^":
        return True
    else:
        return False
    
def prefix_to_infix(prefix):
    stack = []
    for i in range(len(prefix)-1, -1, -1):
        if not is_operator(prefix[i]):
            stack.append(prefix[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            result = f"({op1}{prefix[i]}{op2})"
            stack.append(result)
    return stack.pop()