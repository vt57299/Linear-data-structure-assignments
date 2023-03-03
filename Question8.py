# Q8. Write a program to reverse a stack.

def reverse_stack(stack):
    if not stack:
        return stack
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)
    return stack

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)