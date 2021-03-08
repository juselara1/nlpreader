import time, os, re

from nlpreader.utils import get_words, ner2color
from threading import Thread

class NLPReader(Thread):
    def __init__(
            self, bindings, 
            colors, defaults, text=None
            ):

        self.__text = text

        self.__bindings = bindings
        self.__colors = colors
        self.__defaults = defaults

        self.__wpm = defaults["wpm"]
        self.__interval = 60 / self.__wpm
        
        self.__make_cols(get_words(text))
        
        self.__idx = 0
        self.__running = True

        self.stop = False
        Thread.__init__(self)

    def __make_cols(self, words):
        self.__cols = ner2color(
                words, self.__wpm,
                self.__colors,
                self.__defaults
                )

    def make_action(self, action):
        if len(action) > 1:
            res = re.match(r"(\d+)(\w)", action)
            if res is None:
                return
            num, action = res.groups()
            num = int(num)
        else:
            num = 1

        if action not in self.__bindings:
            return

        if self.__bindings[action] == "nw":
            self.__idx += num if self.__idx < len(self.__cols) - 1 else len(self.__cols) - 1
        elif self.__bindings[action] == "pw":
            self.__idx -= num if self.__idx > 0 else 0

        elif self.__bindings[action] == "wpm+":
            self.__wpm += 8*num if self.__wpm < 2048 else 2048
            self.__interval = 60 / self.__wpm

        elif self.__bindings[action] == "wpm-":
            self.__wpm -= 8*num if self.__wpm > 8 else 8
            self.__interval = 60 / self.__wpm

        elif self.__bindings[action] == "pause":
            self.__running = not self.__running

        elif self.__bindings[action] == "rst":
            self.__idx = 0 

        elif self.__bindings[action] == "quit":
            self.stop = True
            return
        
        self.__make_cols(get_words(self.__text))

    def run(self):
        while not self.stop:
            cols = self.__cols[self.__idx]
            os.system('cls' if os.name == 'nt' else 'clear')
            print(*cols, sep="", end="\r")

            if self.__idx >= len(self.__cols) - 1 or\
                    not self.__running:
                time.sleep(0.1)
                continue

            if self.__running:
                self.__idx += 1

            time.sleep(self.__interval)
