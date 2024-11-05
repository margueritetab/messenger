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


def choix_users():
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
        choix_users()
    else :
        choix_menu()


def choix_channels():
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
        print('x. Main Menu')
        print('')
        choix_channels()
    elif choice == 'x':
        choix_menu()
    else:
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
        choix_channels()
    

def choix_menu():
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
        choix_users()
    else:
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
        print('x. Main Menu')
        print('')
        choix_channels()
choix_menu()