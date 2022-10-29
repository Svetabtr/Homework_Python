import datetime

def log (update, context):
    file = open('log.csv', 'a')
    file.write(f'{datetime.datetime.now()}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()
