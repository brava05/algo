NUMBER_LETTERS = 3
its_first_line = True
letters_set = set()
with open("input.txt") as file:
    firstline = file.readline()
    string_list = file.readlines()

dict_pair = {}
for name in string_list:
    for index in range(len(name)-3):
        
        letter = name[index:index+NUMBER_LETTERS]
        letters_set.add(letter)
        if index < len(name)-4:
            next_letter = name[index+1:index+1+NUMBER_LETTERS]
            pair = f'{letter} {next_letter}'
            dict_pair[pair] = dict_pair.get(pair, 0)+1

with open("output.txt", "w") as output:
    end = '\n'
    output.write(f'{len(letters_set)} {end}')
    output.write(f'{len(dict_pair)} {end}')
    for pair, number in dict_pair.items():
        output.write(f'{pair} {number} {end}')
