# telegram-monitoring

<p align="center">
  <img src="https://github.com/theo-grivel/telegram-monitoring/blob/main/assets/Botpic.png" alt="bot picture"/>
</p>

Monitoring with a telegram bot

## take a talk with the bot father

set this commands
```
disk - disk usage
cpu - cpu load
stats - uptime and ram
who - who is connected
```

## Put your token

replace the  `TOKEN` with the BotFather's token
when you send message to the bot when he is running,
the script will print your chat ID

```
echo telegrambot = \'TOKEN\' >> bot/tokens.py
echo adminchatid = \[chat_id\] >> bot/tokens.py
```

## System daemon

```
mv ./service/telegram_bot.service /etc/systemd/system/
cp -r ./bot /usr/
systemclt daemon-reload
systemclt start telegram-bot
systemclt enable telegram-bot
```
