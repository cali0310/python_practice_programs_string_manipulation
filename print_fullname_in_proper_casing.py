# Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
# input fullname
# set fullname to title case
# print fullname

fullname = str(input("Enter your fullname: "))
fullname = fullname.title()
print(fullname)