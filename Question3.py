# Q3. Write a program to check if two strings are a rotation of each other?

def is_rotation(str1,str2):
    string = str1+str1
    if str2 in string:
        return True
    else:
        return False

a = "print"
b = "intpr"
res = is_rotation(a,b)
print(res)