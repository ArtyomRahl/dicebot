import dice_roller
import faq
import characters
import dungeon

def message(text_message):

    answer = ['']

    if text_message.startswith('!roll '):
        # Бросок кубика
        answer = dice_roller.message(text_message)
    elif text_message.startswith('!help'):
        # Список команд
        answer = faq.message(text_message)
    elif text_message.startswith('!dungeon'):
        # Прохождение подземелья
        answer = dungeon.message(text_message)
    elif text_message.startswith('!'):
        # Команда персонажа в базе
        answer = characters.message(text_message)
    else:
        answer = 'Mistake. !help to read bot command.'

    return answer
