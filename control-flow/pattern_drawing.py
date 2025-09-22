size = int(input("Enter the size of the pattern:"))
i = size
while i > 0:
    for j in range(size):
        print("*", end="")        
    print()    
    i -= 1