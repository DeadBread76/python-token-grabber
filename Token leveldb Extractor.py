import re
import os
import sys
import pyperclip
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
if folder_selected == '':
    sys.exit()
for root, dirs, files in os.walk(folder_selected):
    for file in files:
        with open (folder_selected+'/'+file,  errors='ignore') as handle:
            try:
                lines = handle.readlines()
            except Exception as e:
                print (e)
            for line in lines:
                if '[oken' in line:
                    pattern = r'"([A-Za-z0-9_\./\\-]*)"'
                    token = re.search(pattern, line)
                    tokenfound = token.group().strip('"')
                    print (tokenfound)
                    pyperclip.copy(tokenfound)
                    input()
                    break
                if '>oken' in line:
                    pattern = r'"([A-Za-z0-9_\./\\-]*)"'
                    token = re.search(pattern, line)
                    tokenfound = token.group().strip('"')
                    print (tokenfound)
                    pyperclip.copy(tokenfound)
                    input()
                    break
                if 'token>' in line:
                    pattern = r'"([A-Za-z0-9_\./\\-]*)"'
                    token = re.findall(pattern, line)
                    for string in token:
                        if len(string) < 59:
                            continue
                        else:
                            print (string)
                            pyperclip.copy(string)
                            break
                    input()
                    break
