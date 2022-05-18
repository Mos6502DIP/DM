import random
import socket
from threading import Thread
import os
import time
NullString = "" 
NullInt = "-1"
Indata = True
cache1 = {}

def recv():
    SERVER_HOST = input("SERVER IP: ")
    SERVER_PORT = int(input("Host port: "))
    print("Getting the TCP socket setup.")

    s = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))

    bongo = True
    

    while bongo == True:

        message = s.recv(1024).decode(encoding="utf-8")
        if message == ":'>?":
            print("Download Start")
            bongo = False
    counter = 1
    while eddy == True:
            edit = s.recv(1024).decode(encoding="utf-8")
            if edit[0:2] == ">?":
                        eddy = False
            cache1[counter] = edit
            counter = counter + 1

    s.close
def disp():
    counter = 1
    while counter != int(len(cache1)):
         print(cache1[counter])
         counter += 1

def sendme(data):
    s.send(data.encode())

def send():
    SERVER_HOST = input("SERVER IP: ")
    SERVER_PORT = int(input("Host port: "))
    print("Getting the TCP socket setup.")

    s = socket.socket()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
    s.connect((SERVER_HOST, SERVER_PORT))
    print("transfer started")
    
    sendme = ":'>?"
    s.send(sendme.encode())
    counter = 1
    while counter != int(len(cache1)):
         sendme  = cache1[counter]
         s.send(sendme.encode())
         counter += 1
    sendme = ">?"
    s.send(sendme.encode())
    
   
   

    
    
   
    
    

    


print("""
██████╗░███╗░░░███╗
██╔══██╗████╗░████║
██║░░██║██╔████╔██║
██║░░██║██║╚██╔╝██║
██████╔╝██║░╚═╝░██║
╚═════╝░╚═╝░░░░░╚═╝
Dictionary ,Mangment Using the DTTP ©

""")


while Indata == True:
    
    command = str(input("DDM/>:"))
    
    com = command[0:4]
    command = command + "                  "

    if com == "disp" and  len(command) > 5 :
        com = command[4]
        if com == ",":
            com = command[5:7]
            
            if com == "01":
                 com = command[7]
                 if com == ",":
                     com = command[8]
                     com = int(com)
                     print(cache1[com])
                     
                 else:
                     disp()
                     
                     

            else:
                print("No data base can be found with that idenity.")
    elif com == "help":
            print("""
DDM commands:
disp eg(disp,01,01) displays storage 01 area 0
edit  eg(edit) lets you edit.

DDM edit commands:
<> exit ddm edit
* area change
            """)
            

    elif com == "edit":
        counter = int(input("Start area : "))
        eddy = True

        while eddy == True:
            edit = input("DDM/edit/"+str(counter)+"/>:")
            if edit[0:2] == "<>":
                        eddy = False
            cache1[counter] = edit
            counter = counter + 1
           

    elif com == "wash":
        os.system("cls")

    elif com == "addd":
        print("comming soon")

    elif com == "send":
        print("this mode is unstable and could crash at any moment.")

        check = input("have you saved  [Y, N] :  ")

        if check == "Y" and len(cache1) > 1:
            
            send()

        elif len(cache1) > 1:
            print("No data found to be sent")
            
        else:
            print("send aborted")
    elif com == "recv":
        recv()
        



    elif com == "exit":
        check = input("Have you saved [Y, N] :  ")
        if check == "Y":
            exit("Thank you for using DDM edit you CH database")
        else:
            print("Exit aborted")
            

        
        
            



             

