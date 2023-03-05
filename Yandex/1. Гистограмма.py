# with open("input_gist.txt") as file:

    # while True: 
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line)
# with open("Yandex/input.txt") as file:
# https://contest.yandex.ru/contest/45468/problems/1/

def main():
    
    with open("input.txt") as file:

        dict_letters = {}
        lines = file.readlines()
        for line in lines:
            for letter in line:
                if letter in dict_letters:
                    dict_letters[letter] += 1
                else:
                    dict_letters[letter] = 1
        
        if len(dict_letters) == 0:
            return

        if ' ' in dict_letters:
            del dict_letters[' ']
        if '\n' in dict_letters:
            del dict_letters['\n']

        sorted_letters = sorted(dict_letters.keys())
        max_c = max(dict_letters.values())

        for i in range(max_c):
            for letter in sorted_letters:
                if dict_letters[letter] >= max_c - i:
                    print("#", end='')
                else:
                    print(" ", end='')
            print()
        
        for letter in sorted_letters:
            print(letter, end='')

if __name__ == '__main__':
    main()