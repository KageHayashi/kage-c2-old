from kage.core.constants import BANNER
from kage.core import base
from kage.core import sentinel
from kage.core.common import *

# ===============================================
# Kage Class - The entrypoint menu of the program
# ===============================================

class Kage(base.Base):
    all_sentinels = {}
    
    def __init__(self):
        base.Base.__init__(self)
        self.prompt = "(kage) "

    # ================
    # COMMANDS
    # ================
    def do_list(self, args):
        '''Lists all listeners and their status.'''
        print('Listeners.')

    def do_start(self, args):
        '''Starts a new listener.'''
        try:
            args = args.split()
            name = args[0]
            if name in sentinel.SENTINELS:
                printError(f"Sentinel '{name}' is already active.")
                return
            
            if len(args) == 2:
                port = int(args[1])
                if port in sentinel.PORTS_IN_USE:
                    printError("Port already in use.")
                    return
            elif len(args) == 1:
                if sentinel.PORTS_IN_USE == []:
                    port = 5000
                else:
                    port = sentinel.PORTS_IN_USE[-1] + 1
            
            s = sentinel.Sentinel(name, port)
            s.start()
            print()
            printSuccess(f"Successfully started Sentinel '{name}' on port {port}")
            printInfo(f"Sentinel '{name}' is active at: http://127.0.0.1:{port}\n\r")
        except ValueError:
            printError("Invalid port. Please enter an integer")
            return
        except Exception as e:
            raise
    
    def do_kill(self, args):
        '''Kills a listener.'''
        args = args.split()
        name = args[0]
        try:
            sentinel.SENTINELS[name].kill()
            del sentinel.SENTINELS[name]
        except KeyError:
            printError(f"Sentinel '{name}' is not active.")

    def do_exit(self, args):
        '''Exits the program.'''
        sentinel.killAllSentinels()
        return True
        
    # ==============
    # HELPS
    # ==============
    def help_list(self):
        print(getattr(self, 'do_list').__doc__)
    
    def help_start(self):
        print(getattr(self, 'do_start').__doc__)
        print("start <name> [port]")

    # Other stuff
    def print_banner(self):
        print(BANNER, end='')