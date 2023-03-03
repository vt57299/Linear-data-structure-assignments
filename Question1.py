# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?


def to_find_pairs(array,target):
    pairs = []

    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] +array[j] == target:
                pairs.append((array[i],array[j]))
    return pairs
            

lst = list(map(int,input("Enter List elements seprated by a comma: ").split(",")))
num = int(input("Enter Target number: "))

result = to_find_pairs(lst,num)
print(result)