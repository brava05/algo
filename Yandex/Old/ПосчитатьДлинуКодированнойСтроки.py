first_symbol = True
result = 0
number = ''

for c in input():
    if c.isdigit():
        number += c
    elif c.isalpha() and not number:
        if first_symbol:
            first_symbol = False
        else:
            result += 1
    elif c.isalpha() and number:
        result += int(number)
        number = ''
	
if number:
    result += int(number)
else:
    result += 1
print(result)

# AAAABBB будет сжата в строку A4B3
# строка AAAAAAAAAAAAAAABAAAAA — в строку A15BA5.