import os, sys

RED     = "\u001b[31m"
GREEN   = "\u001b[32m"
YELLOW  = "\u001b[33m"
CYAN    = "\u001b[36m"
RESET   = "\u001b[0m"

def printSuccess(message: str) -> None:
    '''Prints a message in green signifying success.'''
    print(GREEN + "[+] " + message + RESET)

def printError(message: str) -> None:
    '''Prints a message in red signifying error.'''
    print(RED + "[!] " + message + RESET)

def printWarning(message: str) -> None:
    '''Prints a message in yellow signifying warning.'''
    print(YELLOW + "[*] " + message + RESET)

def printInfo(message: str) -> None:
    '''Prints a message in cyan signifying info.'''
    print(CYAN + "[*] " + message + RESET)

def prompt(menu_name: str) -> str:
    '''Creates a prompt for a given menu name'''
    prompt = f"{GREEN}({menu_name}){RESET}> "
    return prompt

def clrScreen():
    '''Clears the screen'''
    os.system("clear")