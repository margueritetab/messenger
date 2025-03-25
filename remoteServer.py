import requests
from model import User, Channel, Message
from client import *
import json

class RemoteServer:
    def __init__(self, url):
        self.url=url

    def users(self)-> list[User]:
        response_users=requests.get(self.url+'/users')
        return(User(user["id"], user["name"]) for user in response_users.json())

    def channels(self)-> list[Channel]:
        response_channels=requests.get(self.url+'/channels')
        return(Channel(channel["id"], channel["name"], channel["member_ids"]) for channel in response_channels.json())

    def messages(self)-> list[Message]:
        response_messages=requests.get(self.url+'/messages')
        return(Message(mess["id"], mess["reception_date"], mess["sender_id"], mess["channel"], mess["content"]) for mess in response_messages.json())
    
    def add_user(self, name):
        requests.post(self.url+'/users/create', json={"name":name})
