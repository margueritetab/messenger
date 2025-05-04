
import json
from model import User, Channel, Message

class Server:
    def __init__(self, filename:str, users:list[User], channels:list[Channel], messages:list[Message]):
        self._filename = filename
        # Si vous avez une fonction `users` dans votre classe,
        # vous ne pouvez pas avoir une variable `users`.
        # Une bonne pratique est de préfixer cette variable par un `_`,
        # ce qui est une convention qui indique aux développeurs
        # qu'il ne faut pas accéder à cette variable depuis l'extérieur
        # de la classe.
        self._users = users
        self._channels = channels
        self._messages = messages
    def __repr__(self) -> str:
        return f'Server(users={self._users}, channels={self._channels}, messages=[{self._messages}])'

    @classmethod
    def load_from_json_file(cls, file_path: str) -> 'Server':
        with open(file_path) as fichier:
            server_dict = json.load(fichier)
        new_server = Server(file_path, [], [], [])
        for user in server_dict['users'] :
            new_server._users.append(User.from_dict(user))
        for channel in server_dict['channels'] :
            new_server._channels.append(Channel.from_dict(channel))
        for message in server_dict['messages'] :
            new_server._messages.append(Message.from_dict(message))
        return new_server

    # En mettant cette fonction dans la classe `Server`, vous pourrez
    # l'appeler à partir d'un objet `server` de la classe `Server`
    # en écrivant `server.save()`
    def save(self):
        new_server = {'users':[], 'channels':[], 'messages':[]}
        for user in self._users :
            new_server['users'].append({'id': user.id, 'name':user.name} )
        for channel in self._channels :
            new_server['channels'].append({'id' : channel.id, 'name' : channel.name, 'member_ids':channel.member_ids})
        for message in self._messages :
            new_server['messages'].append({'id':message.id, 'reception_date':message.reception_date, 'sender_id' : message.sender_id, 'channel':message.channel, 'content':message.content})
        with open(self._filename,'w') as json_file :
            json.dump(new_server,json_file)

    # Comme ces fonctions appartiennent à la classe `Server`, il faut les indenter.
    # Sinon Python n'a aucun moyen de savoir qu'elles font partie de la classe.
    def users(self):
        return(self._users)
    def channels(self):
        return(self._channels)
    def messages(self):
        return(self._messages)

    # Remarquez que cette nouvelle fonction a la même signature
    # (c'est à dire le même nombre et le même type de paramètres et
    # de valeurs de retours) que la fonction `RemoteServer.add_user`.
    # Ca vous permet d'utiliser la fonction `add_user` depuis votre
    # `Client` sans avoir à vous préoccuper de savoir si vous
    # manipulez un `Server` ou un `RemoteServer`
    def add_user(self, name: str) -> User:
        new_id = max([user.id for user in self._users]) + 1
        new_user = User(new_id, name)
        self._users.append(new_user)
        self.save()

        return new_user
