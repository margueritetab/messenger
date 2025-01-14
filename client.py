from server import *
from model import *
from datetime import datetime
from remoteServer import RemoteServer


class Client:
    def __init__(self, server:"RemoteServer"):
        self.server = server
    
    def connexion(self):
        print('Messenger')
        print('---------')
        print('i. inscription')
        print('c. connexion')
        print('x. leave')
        print('')
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'c':
            mon_id = int(input('What is your id? :'))
        elif choice == 'i':
            name = input('What is your name ?')
            mon_id = max([user.id for user in self.server.users]) + 1
            self.server.users.append(User(mon_id, name))
            save_server(self.server)
            print('your id is', mon_id)
            add_user(name)
        elif choice == 'x':
            print('Bye !')
            return None
        else:
            print('Unknown option', choice)
            return self.connexion()
        self.choix_menu(mon_id)

    def choix_users(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            name = input('Choose a name :')
            id = max([user.id for user in self.server.users]) + 1
            self.server.users.append(User(id, name))
            print('User list')
            print('---------')
            print('')
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            print('n. Create user')
            print('x. Main Menu')
            print('')
            save_server(self.server)
            self.choix_users(mon_id)
        else :
            self.choix_menu(mon_id)

    def choix_voir_message(self, mon_id, id_groupe):
        for channel in self.server.channels:
            if channel.id == id_groupe:
                name_groupe = channel.name
        print(name_groupe)
        print('------------------')
        for message in self.server.messages :
            if message.channel == id_groupe:
                reception_date = message.reception_date
                sender_id = message.sender_id
                content = message.content
        for user in self.server.users:
            if user.id == sender_id:
                name = user.name
        print(reception_date)
        print(name, ':', content)
        print('')
        print('s. send a message')
        print('x. return to the channels')
        print('') 

    def choix_message(self, mon_id, id_groupe):
        choice = input('enter a choice and press <Enter>:')
        if choice == 'x':
            self.afficher_channels(mon_id)
            self.choix_channels(mon_id)
        elif choice == 's':
            content = input('What is the message you want to send :')
            copy = self.server.messages.copy()
            for mess in copy:
                if id_groupe == mess.channel:
                    id = max([message.id for message in self.server.messages]) + 1
                    reception_date=datetime.now()
                    self.server.messages.append(Message(id, reception_date, mon_id, id_groupe, content))
            print('')
            print('s. send a message')
            print('x. return to the channels')
            print('')
            save_server(self.server)
            self.choix_message(mon_id, id_groupe)
        else :
            print('Unknown option', choice)
            self.choix_message(mon_id, id_groupe)  

    def afficher_channels(self, mon_id):
        print('Channels list')
        print('---------')
        print('')
        has_channel = False
        for channel in self.server.channels:
            if mon_id in channel.member_ids:
                has_channel = True
                id_users = channel.member_ids
                membres = []
                for user in self.server.users:
                    if user.id in id_users:
                        membres.append(user.name)
                print(channel.id,'.', channel.name, ', membres :', [m for m in membres])
        if has_channel:
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

    def choix_channels(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            id = max([channel.id for channel in self.server.channels]) + 1
            name = input('Choose a channel name :')
            members_name = (input('Members list :'))
            liste_members_name = members_name.split(',')
            liste_members_name_finale = []
            for e in liste_members_name:
                liste_members_name_finale.append(e.strip())
            liste_id = []
            for m in liste_members_name_finale :
                for user in self.server.users:
                    if user.name == m:
                        liste_id.append(user.id)
            self.server.channels.append(Channel(id, name, liste_id))
            for channel in self.server.channels:
                print(channel)
            print('')
            print('n. Create channel')
            print('a. Add a member')
            print('m. See message')
            print('x. Main Menu')
            print('')
            self.choix_channels(mon_id)
            save_server(self.server)
        elif choice == 'x':
            self.choix_menu(mon_id)
        elif choice == 'a':
            groupe_id = int(input('Which channel id ? :'))
            print('')
            print('User list')
            print('---------')
            print('')
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            member_id = int(input('Id of the member you want to add :'))
            for channel in self.server.channels:
                if channel.id == groupe_id:
                    channel.member_ids.append(member_id)
            for channel in self.server.channels:
                print(channel)
            print('')
            print('n. Create channel')
            print('a. Add a member')
            print('x. Main Menu')
            print('')
            save_server(self.server)
            self.choix_channels(mon_id)
        elif choice == 'm':
            id_groupe = int(input('Enter the id of the group :'))
            self.choix_voir_message(mon_id, id_groupe)
        else :
            print('Unknown option', choice)
            self.choix_channels(mon_id)

    def choix_menu(self, mon_id):
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
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            print('n. Create user')
            print('x. Main Menu')
            print('')
            self.choix_users(mon_id)
        elif choice == '2':
            self.afficher_channels(mon_id)
            self.choix_channels(mon_id)
        else:
            print('Unknown option', choice)
            self.choix_menu(mon_id)