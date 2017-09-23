identifier = input('Enter identifer to CamelCap : ')
identifier = identifier.split(' ')
CamelCap = ''
for word in identifier:
    word = word[1] + word[2:]
    CamelCap = CamelCap + word
print(CamelCap)
