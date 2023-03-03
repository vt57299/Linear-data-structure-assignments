# Q4. Write a program to print the first non-repeated character from a string?

def fn(string):
    temp = []
    for i in string.replace(" ",""):
        if string.count(i) ==1:
            temp.append(i)
    return temp[0]

st = input("Enter a string: ")
print(fn(st))