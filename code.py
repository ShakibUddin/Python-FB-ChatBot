from fbchat import Client,log

from fbchat.models import *

import credentials#when you run it create a new python file with the name credentials and put email and password there
import random

class Carnage(Client):

    def onMessage(
        self,
        mid=None,
        author_id=None,
        message=None,
        message_object=None,#the message
        thread_id=None,#user who sent the message
        thread_type=ThreadType.USER,#type of chat person chat or group chat
        **kwargs
    ):
        self.markAsRead(author_id)# mark message as seen
        log.info(f"Message \"{message_object}\" from {thread_id} in {thread_type}")

        msgText=message_object.text

        reply=["Hello, Sakib is not online right now.","Please wait some time...","You can call him at this number if it's emergency 017********"]
        reply2=["I am just a BOT created using Python","I am Carnage, Sakib's personal AI assistant"]
        reply3=["hello","hey","what's up","hi"]


        if author_id!=self.uid:
            msgText=msgText.lower()

            if "who" in msgText or "what" in msgText or "tui ke" in msgText or "tui keda" in msgText:
                ran2 = random.randint(0, 1)
                self.send(Message(text=reply2[ran2]),thread_id=thread_id,thread_type=thread_type)
            elif "hello" in msgText or "hey" in msgText or "kire" in msgText or "oi" in msgText or "sakib" in msgText:
                ran3 = random.randint(0, 2)
                self.send(Message(text=reply3[ran3]), thread_id=thread_id, thread_type=thread_type)
            else:
                ran = random.randint(0, 2)
                self.send(Message(text=reply[ran]), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id,thread_id)#mark reply as delivered

client = Carnage(credentials.email,credentials.password)

client.listen()