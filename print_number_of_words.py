# Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
# input complete statement
# count words in statement
# print number of words

enter_statement = str(input("Enter a complete statement: "))
word_count = len(enter_statement.split())
print("Number of words: ", word_count)