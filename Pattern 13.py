n=int(input())
val=10
for i in range(n):
    for j in range(i+1):
        print(val,end=" ")
        val=val+10
    print()
