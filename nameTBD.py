#Todo: set up a basic "shell" and create a few functions for future web app vulnerability testing
#ideal workflow would be:
#scan for service and version -> automatically search exploitdb -> if not exploitdb, investigate manually and come back
#maybe have some functions for each service?
#example, ssh function has options for brute force,
import os, requests


#Reconnaissance

#Passive Recon
def passiveRecon():
    print("All (1) DNSDumpster(2) ICANN(3) Shodan(4)")
    while True:
        action = int(input("> "))
        if type(action) != int:
            print("Invalid action")
        if action == "1":
            url = "https://api.dnsdumpster.com/domain/"


#read the list of programs in /bin
#if "command" matches with the list of programs in /bin, run that using os.system("command")

#functionChecker + argument parser
def functionChecker(action):
    #insert argument parser here
    #todo: split every word in 'action' by spaces, after removing extra spaces
    #the first word will always be the command, anything after that are args

    args = []

    if action == "passiveRecon":
        passiveRecon(args)
    elif action == "nmap":
        nmap(args)
    elif action == "clear":
        os.system("clear") #find a way to set TERM environment variable

    else: return("Invalid action")

##define functions

def nmap(args):
    return os.system("nmap --version")

def clear():
    return(os.system("clear"))
#the "shell"

while True:
    action = input("> ")
    print("debug" + str(type(action)))
    if action == "exit":
        break
    elif type(action) != "str":
        print("Invalid action")
    functionChecker(action)
