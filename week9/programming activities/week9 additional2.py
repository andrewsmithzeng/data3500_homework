"""
Write a function apple(n,x) that takes in two integers n and x 
and prints out the number of times x appears in the multiplication table of size n x n. 

1       2       3       4       5       6
2       4       6       8       10      12
3       6       9       12      15      18
4       8       12      16      20      24
5       10      15      20      25      30
6       12      18      24      30      36
4

"""

def apple(n,x):
    n = int(n) 
    x = int(x) 
    array = [[i*j for i in range(1,n+1)] for j in range(1,n+1)]
    
    for r in array:
        for c in r:
            print(c,end = "\t")
        print()
    
    
    count = 0
    for r in range(n):
        for c in range(n):
            if array[r][c] == x:
                count += 1
    return print(count)

apple(6,12)
apple(5,20)