# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
# input name in incorrect casing
# set name in pascal case 
# print name

fullname = str(input("Enter your fullname in incorrect casing: ").title())
pascal_case = fullname.replace(" ", "")
print(pascal_case)