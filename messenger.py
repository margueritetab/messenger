from datetime import datetime

import json
with open('server_data.json', 'r') as fichier:
    server = json.load(fichier)

def connexion():
    print('Messenger')
    print('---------')
    print('i. inscription')
    print('c. connexion')
    print('')
    choice = input('Enter a choice and press <Enter>:')
    if choice == 'c':
        mon_id = int(input('What is your id? :'))
    else:
        name = input('What is your name ?')
        mon_id = max([d['id'] for d in server['users']]) + 1
        server['users'].append({'id' : mon_id, 'name' : name})
        print('your id is', mon_id)
    save_server()
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
        save_server()
        choix_users(mon_id)
    else :
        choix_menu(mon_id)

def choix_voir_message(mon_id, id_groupe):
    for d in server['channels']:
        if d['id'] == id_groupe:
            name_groupe = d['name']
    print(name_groupe)
    print('------------------')
    for d in server['messages'] :
        if d['channel'] == id_groupe:
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


def choix_message(mon_id, id_groupe):
    choice = input('enter a choice and press <Enter>:')
    if choice == 'x':
        afficher_channels(mon_id)
        choix_channels(mon_id)
    else :
        content = input('What is the message you want to send :')
        copy = server['messages']
        for d in copy:
            if id_groupe == d['channel']:
                id = max([dic['id'] for dic in server['messages']]) + 1
                server['messages'].append({'id': id, 'reception_date' : 'now','sender_id': mon_id, 'channel' : id_groupe, 'content' : content})
        print('')
        print('s. send a message')
        print('x. return to the channels')
        print('')
        save_server()
        choix_message(mon_id, id_groupe)


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
        save_server()
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
        save_server()
        choix_channels(mon_id)
    else :
        id_groupe = int(input('Enter the id of the group :'))
        choix_voir_message(mon_id, id_groupe)
    

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
        else:
            print('you do not have a channel yet')
            print('')
            print('n. Create channel')
            print('x. Main Menu')
            print('')

def save_server():
    with open('server_data.json', 'r') as fichier:
        json.dump(server, fichier, indent=4, ensure_ascii=False)
connexion()