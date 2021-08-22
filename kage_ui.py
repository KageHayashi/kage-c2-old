from kage.core import kage
from kage.core import constants

if __name__ == '__main__':
    k = kage.Kage()
    k.print_banner()
    k.cmdloop()