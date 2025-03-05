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