
import sqlite3
import json

conn = sqlite3.connect('conv.db')
c = conn.cursor()

c.execute("SELECT data FROM events")

df = c.fetchall()
data = []

for i in df:
    data.append(json.loads(i[0]))

for i in data:
    if i['event'] == 'user':
        print('User : {}'.format(i['text']))
        if len(i['parse_data']['entities']) > 0:
            print('extra data:',i['parse_data']['entities'][0]['entity'],"=",i['parse_data']['entities'][0]['value'])
    elif i['event'] == 'bot':
        print('Bot : {}'.format(i['text']))


