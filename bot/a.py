#!/bin/python3

from tokens import *
import telepot


class YourBot(telepot.Bot):
    def __init__(self, *args, **kwargs):
        super(YourBot, self).__init__(*args, **kwargs)
        self._answerer = telepot.helper.Answerer(self)
        self._message_with_inline_keyboard = None

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        # Do your stuff according to `content_type` ...
        print("Your chat_id:" + str(chat_id)) # this will tell you your chat_id
        if chat_id in adminchatid:  # Store adminchatid variable in tokens.py
            if content_type == 'text':
                if msg['text'] == '/stats' :
                    send_info(chat_id, "stats")
                elif msg['text'] == '/disk' :
                    send_info(chat_id, "disk")
                elif msg['text'] == '/who' :
                    send_info(chat_id, "who")
                elif msg['text'] == '/cpu' :
                    send_info(chat_id, "cpu")
                elif msg['text'] == '/stop' :
                    print ("stop bot")
