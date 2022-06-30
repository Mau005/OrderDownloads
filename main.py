from pystray import Icon, Menu, MenuItem
import subprocess, platform
from PIL import Image
import json
from threading import Thread
import os
import shutil
import sys
import time as tm


class ControlTiempo(Thread):
    def __init__(self, controlHilos, contenido, tiempoActualizar, rutaNueva=None):
        super().__init__()
        self.controlHilos = controlHilos
        self.contenido = contenido
        self.tiempoActualizar = tiempoActualizar
        self.rutaNueva = rutaNueva
        self.contenidoPath = None
        self.rutaActual = None
        self.revisandoRutas()

        self.inicioTiempo = tm.time()
        self.tiempoActual = 0

    def revisandoRutas(self):
        if self.rutaNueva is None:
            self.contenidoPath = os.listdir()
        else:
            self.contenidoPath = os.listdir(self.rutaNueva)
        self.rutaActual = os.getcwd()

    def revisarCarpetas(self):
        for carpetas in self.contenido.keys():
            if not os.path.exists(f"{self.rutaActual}\\{self.contenido[carpetas]['source']}"):
                os.mkdir(f"{self.rutaActual}\\{self.contenido[carpetas]['source']}")

    def revisarExtenciones(self):
        for carpetas in self.contenido.keys():
            extenciones = self.contenido[carpetas]["extencion"]
            rutaMover = self.contenido[carpetas]["source"]

            for ext in extenciones:
                for elementos in self.contenidoPath:
                    if ext in elementos.lower() and not elementos.lower() == "orderdowloads.exe":
                        if self.rutaNueva is None:
                            shutil.move(f"{self.rutaActual}\\{elementos}", f"{self.rutaActual}\\{rutaMover}")
                        else:
                            shutil.move(f"{self.rutaNueva}\\{elementos}", f"{self.rutaActual}\\{rutaMover}")
                self.revisandoRutas()

    def iniciar(self):
        self.revisandoRutas()
        self.revisarCarpetas()
        self.revisarExtenciones()
        self.inicioTiempo = tm.time()

    def run(self):
        self.iniciar()
        while self.controlHilos[0]:
            tiempoTranscurrido = tm.time()
            self.tiempoActual = int(tiempoTranscurrido - self.inicioTiempo)
            if self.tiempoActual >= 60 * self.tiempoActualizar:
                self.iniciar()


class OrderDowloads():
    def __init__(self):
        self.controlHilos = [True, ]
        self.contenido = json.load(open("Config.json", encoding="utf-8"))
        self.enMovimiento = self.contenido["Aplicacion"]["enMovimiento"]
        self.tiempoActualizar = self.contenido["Aplicacion"]["actualizacion"]
        self.rutaNueva = self.contenido["Aplicacion"]["source_new"]

        if len(self.rutaNueva) >= 1:
            self.controlTiempo = ControlTiempo(self.controlHilos, self.contenido["Configuracion"], self.tiempoActualizar,
                                               rutaNueva=self.rutaNueva)
        else:
            self.controlTiempo = ControlTiempo(self.controlHilos, self.contenido["Configuracion"], self.tiempoActualizar)

        self.icon = Icon("OrderDowloads", Image.open("icon.jpeg"), menu=Menu(
            MenuItem("Abrir", Menu(MenuItem("Abrir Contenedor", self.abrirContenedor),
                                   MenuItem("Abrir Documentos", self.abrirDocumentos),
                                   MenuItem("Abrir Videos", self.abrirContenedor),
                                   MenuItem("Abrir Imagenes", self.abrirContenedor),
                                   MenuItem("Abrir Sonidos", self.abrirContenedor),
                                   MenuItem("Abrir Comprimidos", self.abrirContenedor),
                                   MenuItem("Abrir ImagenISO", self.abrirContenedor),
                                   MenuItem("Abrir Programas", self.abrirContenedor),
                                   MenuItem("Abrir Otros", self.abrirContenedor)
                                   )),
            MenuItem("Ejecutar Ahora", self.actualizar),
            MenuItem("Creditos", self.creditos),
            MenuItem("Salir", self.salir)
        ))

    def actualizar(self):
        self.controlTiempo.iniciar()

    def creditos(self):
        self.icon.notify("Esta aplicacion fue echa por Mau", "Creditos: ")


    def abrirArchivo(self, carpeta = None):
        if carpeta is None:
            path = self.controlTiempo.rutaActual
        else:
            path = self.controlTiempo.rutaActual + "/" + carpeta

        if platform.system().lower() == "darwin":
            subprocess.Popen(["open", path])
        elif platform.system().lower() == "windows":
            os.startfile(path)
        else:
            subprocess.Popen(["xdg-open", path])

    def abrirDocumentos(self):
        self.abrirArchivo("Documentos")

    def abrirContenedor(self):
        self.abrirArchivo()

    def salir(self):
        self.controlHilos[0] = False
        self.icon.notify("Se ha cerrado la aplicaciòn Vuelve pronto", "Salida")
        self.icon.stop()

    def iniciar(self):
        self.controlTiempo.start()
        self.icon.notify("Se iniciado OrderDowloads Correctamente", "Mensaje de Inicio")
        self.icon.run()

if __name__ == "__main__":
    app = OrderDowloads()
    app.iniciar()
