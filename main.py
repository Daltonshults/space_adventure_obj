from Controller import Controller
from Interface import Interface
from ReadFile import ReadFile
import sys


def main():
    '''
    Creates an Interface, and ReadFile objects, and passes them into the
    a Controller object it creates. Then runs the run line arg[1]
    '''
    Controller(Interface(), ReadFile())\
        .run(sys.argv[1])


if __name__ == "__main__":
    main()
