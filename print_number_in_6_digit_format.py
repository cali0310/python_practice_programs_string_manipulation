# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# input a number between 0-1000
enter_number = int(input("Input number between 0-1000: "))

if 0 <= enter_number <= 1000:
    # fomat number to a 6-digit format using zfill()
    enter_number = str(enter_number).zfill(6)
    # print number
    print(enter_number)

else:
    print("The program will only accept numbers between 0-1000.")