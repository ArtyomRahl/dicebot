import dice_roller
import math

def message(text_message):
    try:
        message_to_word = text_message.split( )
        name = message_to_word[0]
        name = name[1:]
        answer = ['']
        filename = ['']
        ability = ['']
        dice_n = 1
        dice = 20
        dice_mod = 0
        voskl_i_probel = 2

        chars = open('characters.txt', 'r')
        line = chars.readline()

        for line in chars:
            line_to_word = line.split('|')
            if line_to_word[0] == name:
                filename = line_to_word[2]
                name_len = len(name) + voskl_i_probel
                ability = text_message[name_len:]

        filename = 'char/' + filename
        char = open(filename, 'r')
        line = char.readline()
        for line in char:
            check = line.split('|')
            if line.startswith(ability):
                if check[1] == 'ext':
                    mes = check[2]
                    answer = (dice_roller.message(mes))
                elif check[1] == 'hp':
                    answer.append('HP')
                else:
                    dice_mod = math.floor( (int(check[1]) - 10) / 2)
                    answer = (dice_roller.dice_roller(dice_n, dice, dice_mod))

    except Exception:
        print ('Error')
    return answer
