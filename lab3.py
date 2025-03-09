def check_number():
    num = int(input("Enter a number: "))
    if num % 2 == 1:
        print(num, "is odd.")
    else:
        print(num, "is even.")
        
check_number()