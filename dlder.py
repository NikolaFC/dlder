# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:16:08 2021

@author: nikol
"""
import os
import win32clipboard as clipboard
import you_get
import youtube_dl

print('Checking uptates...Please wait...')
clipboard.OpenClipboard()
Url = clipboard.GetClipboardData()
clipboard.CloseClipboard()
if "youtube.com" in Url:
	cmd="youtube-dl -f 313+251/137+251/137+140/136+140"
	os.system("pip install --upgrade youtube-dl")
else:
	cmd = "you-get" 
	os.system("pip install --upgrade you-get")
currentCMD = cmd + " " + Url
print("start downloading: " + currentCMD)


os.system(currentCMD)
print("Video has been downloaded successfully!(Or might not :D)")
input('Press any key to end')


