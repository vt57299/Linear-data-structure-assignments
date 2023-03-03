# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

'''Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., 
the smallest disk is placed on the top and they are on rod A. 
The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.'''

def T_O_H(n,source,auxilaiary,destination):
    if n == 1:
        print("moved disk 1 from source", source,"to destination", destination)
        return 
    T_O_H(n-1,source,auxilaiary,destination)
    print("moved disk",n, )




T_O_H(1,"A","B","C")