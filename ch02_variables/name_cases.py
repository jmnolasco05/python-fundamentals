name = 'Eric'
# Joan Nolasco 30/03/2024

print(f'Hello, {name}, would you like to learn some Python today?')

print(name.lower())
print(name.upper())
print(name.title())

quote = 'A person who never made a mistake never tried anything new.'
print(f'Albert Einstein once said, "{quote}"')

famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "{quote}"'
print(message)

name_with_spaces = ' \tEric Antonio \nFernandez '
print(name_with_spaces)
print(name_with_spaces.lstrip())
print(name_with_spaces.rstrip())
print(name_with_spaces.strip())


file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))
