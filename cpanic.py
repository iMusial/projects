import importlib
import os
import socket
import subprocess
from pydoc import pager

print("starting cpanic")

#dependency checks
#Built to be modular in a way that if a new dependency is added, it can just be added to this list
dependencies=["requests", "os"]

for dep in dependencies:
    try:
        importlib.import_module(dep)
    except ImportError:
        raise SystemExit(
                "Missing dependency: " + str(dep) + "\n"
                "Suggestion: pip install " + str(dep)
            )

#define functions

def help():
    print("cpanic help page:\n")
    #scan / netmap
    print("scan\nScans for links on the connected machine and adds them to the NetMap\nlimited functionality, just adds an IP to your NetMap for now")
    #connect
    print("connect\nSets a target IP and connects to the NetMap if not already added, sends an ICMP ping and if a reply is received, the 'connection' is set")
    #probe
    print("probe\nCommon port scanning, not nearly as good as nmap. Will probably be an nmap wrapper soon though.")
    #disconnect
    print("disconnect\nunsets current target from an earlier 'connect' command")
    #analyze
    print("analyze\nscans all 65,536 ports, gives detailed information on stateful policy behavior, NAT and routing, firewall vendor, model, and version number, rate limits, response verbosity, and presence/behavior of DPI/SSL inspection")
    #solve
    print("solve\nrequires analyze to be run first, recommends an attack vector by checking service versions for CVEs, and other misconfigurations like anonymous ftp logins or overly-verbose responses")
    #clear
    print("clear\nclears the terminal")
    #note
    print("note\nusage: note [add,rm,edit, list] <filename>\nlet's the user quickly add a note located in /home/documents/cpanicNotes")
    #save
    print("save current session data like nmap scans, analyze outputs, and target info to a text document that can be used to resume the engagement")

def nmap():

    print("starting nmap")

    target = "127.0.0.1"
    port = 631
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))

    if result == 0:
        print("Port {} is open".format(port))

    else:
        print("Port {} is closed".format(port))

#"the shell"
#Greet the user with a command-line like interface including their username

sysUsername = os.environ.get("USER")
while True:
    userBlob = input((sysUsername)+">")
#clean up extra whitespace inbetween words in the user's input, then create a list using the first index as a command and the rest as args
    clean = userBlob.split()
    print("is this a list " + str(clean))

#take the users input, check if the first word in their input is an existing command, then forward them to that function
    commandsList = {"nmap": nmap, "help": help}  # list of functions in this script


    for command in commandsList:
        print(clean[0])
        if clean[0] == command:
            print("yay")
            commandsList[command]()
        else:
            print("nouu")