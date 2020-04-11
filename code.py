from fbchat import Client,log

from fbchat.models import *

import credentials#when you run it create a new python file with the name credentials and put email and password there
#Risky...Leads to temporary account lock

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


        if author_id!=self.uid:#get author id from console
            msgText=msgText.lower()
            reply="ok"
            if author_id=="100026586435660":#This is Rimi's author_id
                self.send(Message(reply), thread_id=thread_id, thread_type=thread_type)

        self.markAsDelivered(author_id,thread_id)#mark reply as delivered

client = Carnage(credentials.email,credentials.password)

client.listen()