
import json
from model import User, Channel, Message

class Server:
    def __init__(self, users:list[User], channels:list[Channel], messages:list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages
    def __repr__(self) -> str:
        return f'Server(users={self.users}, channels={self.channels}, messages=[{self.messages}])'
    @classmethod
    def from_dict(cls, server_dict : dict) -> 'Server':
        new_server = Server([], [], [])
        for user in server_dict['users'] :
            new_server.users.append(User.from_dict(user))
        for channel in server_dict['channels'] :
            new_server.channels.append(Channel.from_dict(channel))
        for message in server_dict['messages'] :
            new_server.messages.append(Message.from_dict(message))
        return new_server
    
def users(self):
    return(self.users)
def channels(self):
    return(self.channels)
def messages(self):
    return(self.messages)

SERVER_FILE_NAME = 'server_data.json'

with open(SERVER_FILE_NAME) as fichier:
    server = json.load(fichier)

def sauv(server):
    with open('server_data.json', "w") as file:
        json.dump(server, file)

server = Server.from_dict(server)

def save_server(server_to_save : Server):
    new_server = {'users':[], 'channels':[], 'messages':[]}
    for user in server_to_save.users :
        new_server['users'].append({'id': user.id, 'name':user.name} )
    for channel in server_to_save.channels :
        new_server['channels'].append({'id' : channel.id, 'name' : channel.name, 'member_ids':channel.member_ids})
    for message in server_to_save.messages :
        new_server['messages'].append({'id':message.id, 'reception_date':message.reception_date, 'sender_id' : message.sender_id, 'channel':message.channel, 'content':message.content})
    with open(SERVER_FILE_NAME,'w') as json_file :
       json.dump(new_server,json_file)
    return new_server