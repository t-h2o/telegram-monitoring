#!/bin/python3

#	/usr/bot/main.py

import subprocess
from tokens import *
import matplotlib
matplotlib.use("Agg") # has to be before any other matplotlibs imports to set a "headless" backend
import matplotlib.pyplot as plt
import psutil
from datetime import datetime
import collections
import time
import telepot



memorythreshold = 85  # If memory usage more this %
poll = 300  # seconds

memlist = []
xaxis = []
settingmemth = []
setpolling = []
graphstart = datetime.now()




def send_info(chat_id, info_type):
    bot.sendChatAction(chat_id, 'typing')
    reply = subprocess.check_output(['/usr/bot/getinfo.sh', info_type])
    bot.sendMessage(chat_id, reply, disable_web_page_preview=True)

def send_alert(chat_id, info_type):
    reply = subprocess.check_output(['/usr/bot/getinfo.sh', info_type])
    bot.sendMessage(chat_id, reply, disable_web_page_preview=True)



#	bot class
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



TOKEN = telegrambot

bot = YourBot(TOKEN)
bot.message_loop()
tr = 0
xx = 0
# Keep the program running.
while 1:
    if tr == poll:
        tr = 0
        timenow = datetime.now()
        memck = psutil.virtual_memory()
        mempercent = memck.percent
        if len(memlist) > 300:
            memq = collections.deque(memlist)
            memq.append(mempercent)
            memq.popleft()
            memlist = memq
            memlist = list(memlist)
        else:
            xaxis.append(xx)
            xx += 1
            memlist.append(mempercent)
        memfree = memck.available / 1000000
        if mempercent > memorythreshold:
            memavail = "Available memory: %.2f GB" % (memck.available / 1000000000)
            graphend = datetime.now()
            tmperiod = "Last %.2f hours" % ((graphend - graphstart).total_seconds() / 3600)
            for adminid in adminchatid:
                bot.sendMessage(adminid, "CRITICAL! LOW MEMORY!\n" + memavail)
                bot.sendPhoto(adminid, plotmemgraph(memlist, xaxis, tmperiod))
    time.sleep(10)  # 10 seconds
    tr += 10
