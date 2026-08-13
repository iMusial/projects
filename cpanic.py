import importlib
import os
import socket
import subprocess
from pydoc import pager

print("starting cpanic")

#define functions

def help():
    print("cpanic help page:\n")
    #scan / netmap
    print("scan\nadds an IP to your NetMap, issues an ICMP echo ping")
    #connect
    print("\nconnect\nSets a target IP and connects to the NetMap if not already added")                                                                                  #probe                                                                             print("\nprobe\nCommon port scanning")
    #disconnect
    print("\ndisconnect\nunsets current target from an earlier 'connect' command")
    #analyze
    print("\nanalyze\nscans all 65,536 ports and service versions, best used before analyze")
    #solve
    print("\nsolve\nrequires analyze to be run first, recommends an attack vector by checking service versions for CVEs, and other misconfigurations like anonymous ftp logins or overly-verbose responses")
    #clear                                                                             print("\nclear\nclears the terminal")
    #note
    print("\nnote\nusage: note [add,rm,edit, list] <filename>\nlets the user quickly add a note located in /home/documents/cpanicNotes")
    #save
    print("\nsave\n saves current session data like nmap scans, analyze outputs, and target info to a text document that can be used to resume the engagement\n")

def nmap():

    print("starting nmap")

    target = ""
    port = ""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))

    if result == 0:
        print("Port {} is open".format(port))

    else:
        print("Port {} is closed".format(port))

def probe():

#"the shell"
#Greet the user with a command-line like interface including their username

        envUSER = os.environ.get("USER")                                                   envPWD = os.environ.get("PWD")
while True:
    unparsedInput = input(envUSER+"@"+socket.gethostname()+"$"+envPWD+">")
    if unparsedInput == "exit" or unparsedInput == "quit":
        exit()
    #clean up extra whitespace inbetween words in the user's input, then create a list using the first word as a command and the rest as args
    unparsedInputClean = unparsedInput.split()

    #take the users input, check if the first word in their input is an existing command, then forward them to that function                                              print("debug: current command is " + unparsedInputClean[0])
    commandsList = {"nmap": nmap, "help": help}  # list of functions in this script


    for command in commandsList:
        if unparsedInputClean[0] == command:
            commandsList[command]() #when a matching command is found, treat commandList[command] as the name of a function.
            break
        else:
            if command == unparsedInputClean[-1]:
                print("command " + unparsedInputClean[0] + " not found.")
