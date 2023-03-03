# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def rev_arr(arr):
    arr = arr[::-1]
    return arr


lst = list(map(int,input("Enter List elements seprated by a comma: ").split(",")))

result = rev_arr(lst)
print(result)