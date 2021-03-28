import ftplib
import sys
import os

def login():
    print("username: ", end="")
    username = input()
    print("password: ", end="")
    password = input()
    try:
        ftp.login(username, password)
    except ftplib.Error:
        print("incorrect login or password")

def list():
    data = []
    ftp.dir(data.append)
    #ftp.quit()
    for line in data:
        a = line.split()
        a = a[8:]
        print("-", *a)

def cwd():
    data = []
    print("filename: ", end="")
    s = input()
    try:
        ftp.cwd("/" + s + "/")         # change directory to /pub/
    except ftplib.Error:
        print("incorrect filename")
    else:
        print("success")
        
def download():
    print("filename: ", end="")
    s = input()
    try:
        ftp.retrbinary("RETR " + s ,open(s, 'wb').write)
    except ftplib.Error:
        print("not enough privileges")
    else:
        print("downloaded")

def upload():
    print("filename: ", end="")
    s = input()
    try:
        ftp.storbinary("STOR " + s, open(s, "rb"), 1024) 
    except ftplib.Error:
        print("not enough privileges")
    else:
        print("uploaded")
        
def logout():
    ftp.login()
    
ftp = ftplib.FTP("127.0.0.1")
logout()
while(True):
    s = input()
    try:
        eval(s + "()")
    except:
        print("incorrect command")