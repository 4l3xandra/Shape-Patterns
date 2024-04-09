# inverted triangle pattern using asterisks (*) and dots (.)

while True:
    user_input = input("Give n (1-20) or press Enter to exit: ")
    if user_input.strip() == "":
        break
    n = int(user_input)
    if n <= 20 and n > 0:
        for i in range(n):
            for j in range(i+1):
                print('*', end=" ")
            for j in range(i+1,n):
                print(".", end=" ")
            for j in range(i,n): 
                print(".", end=" ")
            for j in range(i+1):
                print("*", end=" ")
            print()
    else:
        print("Invalid input. Please ensure n is between 1 and 20.")
