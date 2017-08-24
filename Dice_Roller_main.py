import time
import vk_api

import read_command # Модуль для обработки строки и последующей работы с переменными

# Авторизация
vk = vk_api.VkApi(login = 'your_login', password = 'your_password')
vk.auth()

values = {'out': 0,'count': 100,'time_offset': 60}  # Последние сообщения за 60 секунд (Не более 100)

# Отправка сообщений
def write_message( message, body):
    if 'chat_id' in item:   # В беседу
        vk.method('messages.send', {'chat_id':item[u'chat_id'],'message':message,'body':body})
    else:   # В личные сообщения
        vk.method('messages.send', {'user_id':item[u'user_id'],'message':message,'body':body})

# Прием сообщений
while True:
    response = vk.method('messages.get', values)
    if response['items']:
        # Чтобы работать только с новыми сообщениями
        values['last_message_id'] = response['items'][0]['id']

    for item in response['items']:
        text_message = item[u'body']

        if text_message.startswith('!'):
            try:
                answer = read_command.message(text_message)
                write_message( (' '.join(map(str, answer))), item[u'body'] )
            except Exception:
                try:
                    write_message('Mistake. Enter !help for display the list of commands', item[u'body'] )
                finally:
                    print ('Error')
    time.sleep(1)
