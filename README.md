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

## Notifications

### new connection

When you connect via ssh, this script run once,
```/etc/ssh/sshrc```, you can code inside a send message to the admin.

## Monitoring

Send few informations about state of computer

## Command

### uptime

indicate how many time the machine is running

### ram

indicate how many space is used

### df

display xx% is fill the ```/home```
```
df | grep /home | awk '{print $5}'
```
