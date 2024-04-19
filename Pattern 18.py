def print_pattern18(rows):
    spaces = 0
    stars = rows * 2 - 1 
    for i in range(rows):
        for j in range(spaces):
            print(" ", end=" ")
        for j in range(stars):
            print("*", end=" ") 
        print()
        spaces += 1
        stars -= 2
rows = int(input())
print_pattern18(rows)
