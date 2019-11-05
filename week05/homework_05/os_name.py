# Function gives OS name
import sys


def my_os():
    if sys.platform == 'linux' or sys.platform == 'linux2':
        # linux
        os_name = 'ОС Linux'
    elif sys.platform == 'darwin':
        # mac
        os_name = 'ОС macOS'
    elif sys.platform == 'win32':
        # Windows...
        os_name = 'ОС Windows'
    else:
        os_name = sys.platform
    return os_name
