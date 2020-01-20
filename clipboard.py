from time import sleep
from classes.py_clipboard import Clipboard

clipboard = Clipboard()

while True:
    clipboard.clipboard_manager()
    sleep(2)
