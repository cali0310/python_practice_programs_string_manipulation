# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
# input fullname in incorrect casing
# use swapcase to reverse case
# print fullname

fullname = str(input("Enter your fullname: "))
fullname = fullname.swapcase()
print(fullname)
