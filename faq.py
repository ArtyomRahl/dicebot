def message(text_message):
    answer = ['']
    if text_message.startswith('!help'):
        try:
            faq = open('faq.txt', 'r')
            line = faq.readline()
            for line in faq:
                answer.append (line)
        except Exception:
            print ('Error')

    return answer