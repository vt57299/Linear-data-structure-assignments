# Q7. Write a program to check if all the brackets are closed in a given code snippet.

def check_brackets(code):
    stack = []
    for i in code:
        if i in ["(", "{", "["]:
            stack.append(i)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if i != ")":
                    return False
            if current_char == '{':
                if i != "}":
                    return False
            if current_char == '[':
                if i != "]":
                    return False
  
    if stack:
        return False
    return True