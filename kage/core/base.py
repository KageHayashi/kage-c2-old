#!/usr/bin/python3

import cmd, sys, os

class Colors(object):
    N = '\033[m'   # native
    R = '\033[31m' # red
    G = '\033[32m' # green
    O = '\033[33m' # orange
    B = '\033[34m' # blue


# ======================================================
# Base Class - All menus derive from this base framework
# ======================================================

class Base(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(base) '
        self.spacer = ' '
        self.ruler = '-'
        self.do_help.__func__.__doc__ = '''Displays this menu'''

    def emptyline(self):
        # disables running of last command when no command is given
        # return flag to tell interpreter to continue
        return 0
    
    # ================
    # Commands
    # ================
    def do_hello(self, arg):
        '''Prints the hello intro'''
        print('Hello!')

    def do_exit(self, arg):
        '''Exits the program'''
        # print(f'{Colors.B}Bye.{Colors.N}')
        return True

    # ================
    # Helps
    # ================
    def help_hello(self):
        print('Prints hello message')
    
    def help_exit(self):
        print(getattr(self, 'do_exit').__doc__)

    # A prettier help menu
    def print_topics(self, header, cmds, cmdlen, maxcol):
        if cmds:
            self.stdout.write(f"{header}{os.linesep}")
            if self.ruler:
                self.stdout.write(f"{self.ruler * len(header)}{os.linesep}")
            for cmd in cmds:
                self.stdout.write(f"{cmd.ljust(15)} {getattr(self, 'do_' + cmd).__doc__}{os.linesep}")
            self.stdout.write(os.linesep)

if __name__ == '__main__':
    test_base = Base()
    test_base.cmdloop()
