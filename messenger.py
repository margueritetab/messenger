from datetime import datetime

server = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 1, 'name': 'Town square', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi 👋'
        }
    ]
}

def connexion():
    print('Messenger')
    print('---------')
    print('connexion')
    print('---------')
    mon_id = int(input('What is your id?' :))
    choix_menu(mon_id)

def choix_users(mon_id):
    choice = input('Enter a choice and press <Enter>:')
    if choice == 'n':
        name = input('Choose a name :')
        id = max([d['id'] for d in server['users']]) + 1
        server['users'].append({'id' : id, 'name' : str(name)})
        print('User list')
        print('---------')
        print('')
        for d in server['users']:
            print(d['id'],'.', d['name'])
        print('')
        print('n. Create user')
        print('x. Main Menu')
        print('')
        choix_users(mon_id)
    else :
        choix_menu(mon_id)

def choix_voir_message(mon_id):
    groupe = int(input('Enter the id of the group :'))
    print(groupe)
    print('------------------')
    for d in server['messages'] :
        if d['channel'] == groupe:
            reception_date = d['reception_date']
            sender_id = d['sender_id']
            content = d['content']
    for d in server['users']:
        if d['id'] == sender_id:
            name = d['name']
    print(reception_date)
    print(name, ':', content)
    print('')
    print('s. send a message')
    print('x. return to the channels')
    print('')
    choix_message(mon_id)


def choix_message(mon_id, groupe):
    choice = input('enter a choice and press <Enter>:')
    if choice == 'x':
        print('Channels list')
        print('---------')
        print('')
        for d in server['channels']:
            id_users = d['member_ids']
            membres = []
            for dic in server['users']:
                if dic['id'] in id_users:
                    membres.append(dic['name'])
            print(d['id'],'.', d['name'], ', membres :', [m for m in membres])
        print('')
        print('n. Create channel')
        print('a. Add a member')
        print('m. See message')
        print('x. Main Menu')
        print('')
        choix_channels(mon_id)
    else :
        sender_id = int(input('What is your id ? :'))
        content = input('What is the message you want to send :')
        for d in server['messages']:
            if groupe == d['channel']:
                id = max(dic['id'] for dic in server['message']) + 1
                d.append({'id': id, 'reception_date' : datetime.now(),'sender_id': sender_id, 'channel' : groupe, 'content' : content})







def choix_channels(mon_id):
    choice = input('Enter a choice and press <Enter>:')
    if choice == 'n':
        id = max([d['id'] for d in server['channels']]) + 1
        name = input('Choose a channel name :')
        members_name = (input('Members list :'))
        liste_members_name = members_name.split(',')
        liste_members_name_finale = []
        for e in liste_members_name:
            liste_members_name_finale.append(e.strip())
        liste_id = []
        for m in liste_members_name_finale :
            for d in server['users']:
                if d['name'] == m:
                    liste_id.append(d['id'])
        server['channels'].append({'id' : id, 'name' : str(name), 'member_ids' : liste_id})
        for d in server['channels']:
            print(d)
        print('')
        print('n. Create channel')
        print('a. Add a member')
        print('m. See message')
        print('x. Main Menu')
        print('')
        choix_channels(mon_id)
    elif choice == 'x':
        choix_menu(mon_id)
    elif choice == 'a':
        groupe_id = int(input('Which channel id ? :'))
        print('')
        print('User list')
        print('---------')
        print('')
        for d in server['users']:
            print(d['id'],'.', d['name'])
        print('')
        member_id = int(input('Id of the member you want to add :'))
        for dic in server['channels']:
            if dic['id'] == groupe_id:
                dic['member_ids'].append(member_id)
        for d in server['channels']:
            print(d)
        print('')
        print('n. Create channel')
        print('a. Add a member')
        print('x. Main Menu')
        print('')
        choix_channels(mon_id)
    else :
        print('Channels list')
        print('---------')
        print('')
        for d in server['channels']:
            id_users = d['member_ids']
            membres = []
            for dic in server['users']:
                if dic['id'] in id_users:
                    membres.append(dic['name'])
            print(d['id'],'.', d['name'], ', membres :', [m for m in membres])
        choix_voir_message(mon_id)
    

def choix_menu(mon_id):
    print('=== Messenger ===')
    print('')
    print('1. See users')
    print('2. See channels')
    print('')
    print('x. Leave')
    print('')
    choice = input('Select an option: ')
    print('')
    if choice == 'x':
        print('Bye !')
        return None
    elif choice == '1':
        print('User list')
        print('---------')
        print('')
        for d in server['users']:
            print(d['id'],'.', d['name'])
        print('')
        print('n. Create user')
        print('x. Main Menu')
        print('')
        choix_users(mon_id)
    else:
        afficher_channels(mon_id)
        choix_channels(mon_id)

def afficher_channels(mon_id):
    print('Channels list')
    print('---------')
    print('')
    for d in server['channels']:
        if mon_id in d['member_ids']:
            id_users = d['member_ids']
            membres = []
            for dic in server['users']:
                if dic['id'] in id_users:
                    membres.append(dic['name'])
            print(d['id'],'.', d['name'], ', membres :', [m for m in membres])
    print('')
    print('n. Create channel')
    print('a. Add a member')
    print('m. See message')
    print('x. Main Menu')
    print('')
connexion()