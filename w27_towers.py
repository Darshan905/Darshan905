def hanoi (n, start, middle, end):
    if n == 1:
        print (start, "to", end)
    else:
        hanoi(n-1, start, end, middle)
        print(start, "to", end)
        hanoi(n-1, middle, start, end)
hanoi(8,0,1,2)
