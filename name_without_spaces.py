# input full name with spaces
# remove the left padded spaces in name string using lstrip.()
# print name

user_name = str(input("Enter your name with several space at the beginning: "))
user_name = user_name.lstrip()
print(user_name)