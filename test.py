
import sqlite3
import json

conn = sqlite3.connect('conv.db')
c = conn.cursor()

c.execute("SELECT sender_id, data FROM events")

df = c.fetchall()
sender_id = []
data = []
j = ' '

for i in df:
    sender_id.append(i[0])
    data.append(json.loads(i[1]))

for i in sender_id:
  if j is not i:
    print('===================================================================================================')
  print(i)
  for i in data:
    if i['event'] == 'user':
        print('User : {}'.format(i['text']))
        if len(i['parse_data']['entities']) > 0:
            print('extra data:',i['parse_data']['entities'][0]['entity'],"=",i['parse_data']['entities'][0]['value'])
    elif i['event'] == 'bot':
        print('Bot : {}'.format(i['text']))
  j = i
print('===================================================================================================')
