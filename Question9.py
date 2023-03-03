# Q9. Write a program to find the smallest number using a stack.

def smallest_num(stack):
    if not stack:
        return None
    smallest = stack.pop()
    while stack:
        current = stack.pop()
        if current < smallest:
            smallest = current
    return smallest

print(smallest_num([]))