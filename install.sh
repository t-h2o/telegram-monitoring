# install package
apt install pip
apt install python3

# install python package
pip install python-telegram-bot

# Copy the script in the home in .bot-telegram
cp -r ./srcs/bot /root/.bot-telegram

#	Copy the bot service config
sudo cp ./srcs/bot_debian.service /etc/systemd/system/

#	Start the bot
sudo systemctl deamon-reload
sudo systemctl start bot_debian
