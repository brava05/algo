str_source = input()
str_source = str_source.lower()
str1 = ''
str2 = ''
for i in str_source:
    if i.isdigit() or i.isalpha():
        str1 += i
        str2 = i+str2

print(str1 == str2)