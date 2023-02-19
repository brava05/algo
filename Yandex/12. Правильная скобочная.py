def is_correct_bracket_seq(str1):
    square = 0
    cercle = 0
    figure = 0

    stek = []
    list_str = list(str1)
    for i in list_str:
        if i == "[":
            stek.append(i)
            square += 1
        elif i == "]":
            square -= 1
            if not stek or stek[-1] != "[":
                return "no"
            stek.pop()
        elif i == "(":
            stek.append(i)
            cercle += 1
        elif i == ")":
            cercle -= 1
            if not stek or stek[-1] != "(":
                return "no"
            stek.pop()
        elif i == "{":
            stek.append(i)
            figure += 1
        elif i == "}":
            figure -= 1
            if not stek or stek[-1] != "{":
                return "no"
            stek.pop()
        
        if square<0 or cercle<0 or figure<0:
            return "no"

    if square!=0 or cercle!=0 or figure!=0:
            return "no"
    return "yes"

def main():
    str1 = input()
    print(is_correct_bracket_seq(str1))

if __name__ == '__main__':
    main()
