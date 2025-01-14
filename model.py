
class User:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    def __repr__(self) -> str:
        return f'User(id={self.id}, name={self.name})'
    @classmethod
    def from_dict(cls, user_dict: dict) ->'User':
        return cls(user_dict['id'], user_dict['name'])
    
class Channel:
    def __init__(self, id:int, name:str, member_ids:list):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self) -> str:
        return f'Channel(id={self.id}, name={self.name}, member_ids={self.member_ids})'
    @classmethod
    def from_dict(cls, channel_dict: dict) ->'Channel':
        return cls(channel_dict['id'], channel_dict['name'], channel_dict['member_ids'])
    

class Message:
    def __init__(self, id:int, reception_date:str, sender_id:int, channel:int, content:str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    def __repr__(self) -> str:
        return f'Message(id={self.id}, reception_date={self.reception_date}, sender_id={self.sender_id}, channel={self.channel}, content={self.content})'
    @classmethod
    def from_dict(cls, message_dict: dict) ->'Message':
        return cls(message_dict['id'], message_dict['reception_date'], message_dict['sender_id'], message_dict['channel'], message_dict['content'])
