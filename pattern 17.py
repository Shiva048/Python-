def alphapat(n):
    num = 65
    spaces=0
    stars = n
    for i in range(n):
        for j in range(spaces):
            print(" ", end=" ")
        for j in range(stars):
            ch = chr(num)
            print(ch, end=" ")
            num += 1
        num = 65
        
        print()
        
        
        spaces += 1
        stars -= 1
n = int(input())
alphapat(n)
