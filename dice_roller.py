import random

def message(text_message):

    dice_n = 0
    dice = 0
    dice_mod = 0
    answer = ['']

    if text_message.startswith('!roll '):
        try:
            message_to_word = text_message.split( )
            if message_to_word[0] == '!roll' and len(message_to_word) > 1:
                dices = message_to_word[1].split('d')
                if len(dices) > 1:
                    for i in range (len(message_to_word[1])):
                        if (47 < ord(message_to_word[1][i]) < 58) or (message_to_word[1][i] == 'd'):
                            if message_to_word[1][0] == 'd':
                                dice_n = 1
                                dice = int(dices[1])
                            else:
                                dice_n = int(dices[0])
                                dice = int(dices[1])

                            if len(message_to_word) > 3:
                                if message_to_word[2][0] == '+':
                                    dice_mod = int(message_to_word[3][0:])
                                elif message_to_word[2][0] == '-':
                                    dice_mod = int(message_to_word[3][0:])
                                    dice_mod = - dice_mod
            answer = dice_roller(dice_n, dice, dice_mod)
        except Exception:
            print ('Error')

    return answer

def dice_roller(dice_n, dice, dice_mod):
    dice_sum = 0
    crit_s = 0
    crit_f = 0
    answer = [' ']

    if dice_n > 1:
        answer = ['(']
    else:
        answer = [' ']

    for i in range(dice_n):
        if dice > 0:
            dice_roll = random.randint(1,dice)
            dice_sum += dice_roll
            if (dice == 20) and (dice_roll == 20) and (dice_n < 3):
                crit_s = 1
            if (dice == 20) and (dice_roll == 1) and (dice_n < 3):
                crit_f = 1
            if i == 100:
                answer.append('...')
            elif i < 100:
                answer.append(dice_roll)
                if i < dice_n - 1:
                    answer.append('+')

    if dice_n > 1:
        answer.append(')')

    if dice_mod > 0:
        dice_sum += dice_mod
        answer.append('+')
        answer.append(dice_mod)
    elif dice_mod < 0:
        dice_sum += dice_mod
        answer.append('-')
        answer.append(-dice_mod)
    if dice_sum < 0:
        dice_sum = 0

    if (dice_n > 1) or (dice_mod != 0):
        answer.append('=')
        answer.append(dice_sum)

    if (crit_s == 1):
        answer.append('(Critical success!)')
    if (crit_f == 1):
        answer.append('(Crititcal fail!)')

    return answer