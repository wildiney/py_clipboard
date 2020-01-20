import os
import pyperclip
from datetime import datetime


class Clipboard:
    def __init__(self):
        self.clipboard = []

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def clipboard_manager(self):
        clippedText = pyperclip.paste()
        if not self.clipboard:
            self.clipboard.append({"ct": clippedText, "time": datetime.now()})
            self.view_clipboard()
        else:
            if clippedText != self.clipboard[0]["ct"]:
                self.clipboard.insert(
                    0, {"ct": clippedText, "time": datetime.now()})
                self.view_clipboard()

    def view_clipboard(self):
        self.cls()
        for idx, item in enumerate(self.clipboard):
            itens = len(self.clipboard)
            index = itens - idx
            print(
                "\r\n===========================[{:d} - {:%H:%M:%S}]===========================\r\n".format(
                    index, item["time"]))
            print(item["ct"])
