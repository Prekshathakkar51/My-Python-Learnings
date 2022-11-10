'''USe the template and write the program'''

letter = '''Dear <|name|>,
You are selected!
<|Date|>'''

a = input("Enter your name: ")
b = input("Enter date in dd/mm/yyyy: ")

letter = letter.replace('<|name|>', a)
letter = letter.replace('<|Date|>', b)

print(letter)
