import time
import vk_api
import dice_roller
import faq
import characters

vk = vk_api.VkApi(login = '+799999999999', password = '***************')
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}

def write_message( message, body):
    if 'chat_id' in item:
        vk.method('messages.send', {'chat_id':item[u'chat_id'],'message':message,'body':body})
    else:
        vk.method('messages.send', {'user_id':item[u'user_id'],'message':message,'body':body})



while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        text_message = item[u'body']

        if text_message.startswith('!'):
            try:
                if text_message.startswith('!'):
                    answer = characters.message(text_message)
                if text_message.startswith('!roll '):
                    answer = dice_roller.message(text_message)
                if text_message.startswith('!help'):
                    answer = faq.message(text_message)

                write_message( (' '.join(map(str, answer))), item[u'body'] )
            except Exception:
                try:

                    write_message('Mistake. Enter !help for display the list of commands', item[u'body'] )

                finally:
                    print ('Error')
    time.sleep(1)
