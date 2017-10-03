import vk_api
import time
import vk

#Аутентификация от имени группы
vk = vk_api.VkApi(token='76731ab228f518d2b7efefb61626cb36725693ca762f147bac6aae74381d403ce1ab8bea0c2af6c1d2a53')
vk._auth_token()

values = {'out':0,'count':100, 'time_offset':60}
valuesForGroupMembers ={'group_id' : 'zrc_merch' , 'sort' : 'time_asc' , 'offset' : 0}
valuseForUsers={}

def send_msg(usr_id, msg):
    vk.method('messages.send',{'user_id':usr_id, 'message':msg})

while True:
    members = vk.method('groups.getMembers',valuesForGroupMembers)
    #print(members)
    response = vk.method('messages.get', values)  # ответ
    if response['items']:
        values['last_message_id']=response['items'][0]['id']
    for item in response['items']:
        #send_msg(item['user_id'],'Hello!')
        if response ['items'][0]['body'] != '1':
            _user = vk.method('users.get', {'user_id': response['items'][0]['user_id'], 'name_case': 'nom'})
            _name = _user[0]['first_name']
            send_msg(item['user_id'],'Здорова, '+_name+', я зрк-бот бля! ')
            if response['items'][0]['user_id'] == 117520330 :
                send_msg(item['user_id'], 'Выбери команду: \n 1-написать всем членам сообщества')
        else:
            if response['items'][0]['user_id'] == 117520330:
                for member in members['items']:
                    try:
                        print(member)
                        user = vk.method('users.get',{'user_id':member,'name_case':'nom'})
                        name = user[0]['first_name']
                        print(name)
                        send_msg(member, 'Здорова, '+name+',я зрк-бот бля. Закрой рот! Это тестовое сообщение, можешь идти нахуй.')
                    except:
                        print('Нельзя без диалога')
    time.sleep(1)
