from random import randint
variable = randint(1,67)
file_variable = open('quotes.txt', 'r')
content = file_variable.read().split('/')
print(content[variable])