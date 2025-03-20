# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
# input fullname
# set fullname to snake casing
# print fullname

fullname = str(input("Enter your fullname in incorrect casing: ").lower())
snake_case = fullname.replace(" ", "_")
print(snake_case)