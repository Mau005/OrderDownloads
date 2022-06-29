import json
import os
import shutil
import sys
import time as tm
from threading import Thread

DAEMON = [True, ]


def close():
    print("Close App")
    sys.exit(0)


class ControlTime(Thread):
    def __init__(self, daemon, contents, final):
        super().__init__()
        self.currentPath = None
        self.contenidoPath = None
        self.contents = contents
        self.checkFiles()
        self.checkFileMove()
        self.initialTime = tm.time()
        self.daemon = daemon
        self.timeNow = 0

        self.finalTime = final

    def checkExtensions(self):
        for files in self.contents.keys():
            extencion = self.contents[files]["extencion"]
            pathMove = self.contents[files]["source"]
            for ext in extencion:
                for element in self.contenidoPath:
                    if ext in element.lower():
                        shutil.move(f"{self.currentPath}\{element}", f"{self.currentPath}\{pathMove}")
            self.checkFiles()

    def checkFileMove(self):
        for files in self.contents.keys():
            if not os.path.exists(f"{self.currentPath}\{self.contents[files]['source']}"):
                os.mkdir(f"{self.currentPath}\{self.contents[files]['source']}")

    def checkFiles(self):
        self.contenidoPath = os.listdir()
        self.currentPath = os.getcwd()

    def initProgam(self):
        self.checkFileMove()
        self.checkFiles()
        self.checkExtensions()
        self.initialTime = tm.time()

    def start(self):
        self.initProgam()
        while self.daemon[0]:
            currentTime = tm.time()
            self.timeNow = int(currentTime - self.initialTime)
            if self.timeNow == 60 * self.finalTime:
                self.initProgam()

    def close(self):
        self.daemon[0] = False


class OrderDowloads:

    def __init__(self, daemon):
        self.daemon = daemon
        self.contents = json.load(open("Config.json", encoding="utf-8"))
        self.enMovements = self.contents["Aplicacion"]["enMovimiento"]
        self.finalTime = self.contents["Aplicacion"]["actualizacion"]
        self.daemon[0] = self.enMovements
        self.controltime = ControlTime(self.daemon, self.contents["Configuracion"], self.finalTime)

    def run(self):
        self.controltime.start()
        while self.daemon[0]:
            print(self.controltime.timeNow)
        close()


if __name__ == "__main__":
    app = OrderDowloads(DAEMON)
    app.run()
    DAEMON[0] = False
    close()
