import json
import os
import platform
import shutil
import subprocess
import time
import sys
import time as tm
import webbrowser
from threading import Thread

from PIL import Image
from pystray import Icon, Menu, MenuItem


class ControlTiempo(Thread):
    def __init__(self, icon, controlHilos, contenido, tiempoActualizar, rutaNueva=None):
        super().__init__()
        self.icon = icon
        self.controlHilos = controlHilos
        self.contenido = contenido
        self.tiempoActualizar = tiempoActualizar
        self.rutaNueva = rutaNueva
        self.contenidoPath = None
        self.rutaActual = None
        self.revisandoRutas()
        self.tiempoActual = tm.time()


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
        self.icon.notify("Se han guardado todos los elementos", "Aviso de Ejecución")


    def run(self):
        self.iniciar()
        while self.controlHilos[0]:
            tiempoTranscurrido = tm.time()
            tiempo = tiempoTranscurrido - self.tiempoActual
            print(f"TIempo es: {tiempo}")
            if tiempo >= 60 * self.tiempoActualizar:
                self.tiempoActual = tm.time()
                self.iniciar()
            time.sleep(5)


class OrderDowloads():
    def __init__(self):
        archivo = open("Config.json", encoding="utf-8")
        self.contenido = json.load(archivo)
        archivo.close()
        self.controlHilos = [self.contenido["Aplicacion"]["enMovimiento"], ]
        self.tiempoActualizar = self.contenido["Aplicacion"]["actualizacion"]
        self.rutaNueva = self.contenido["Aplicacion"]["source_new"]
        self.icon = Icon("OrderDowloads", Image.open("icon.jpeg"), menu=Menu(
            MenuItem("Abrir", Menu(MenuItem("Abrir Contenedor", self.abrirContenedor),
                                   MenuItem("Abrir Documentos", self.abrirDocumentos),
                                   MenuItem("Abrir Videos", self.abrirVideos),
                                   MenuItem("Abrir Imagenes", self.abrirImagenes),
                                   MenuItem("Abrir Sonidos", self.abrirSonidos),
                                   MenuItem("Abrir Comprimidos", self.abrirComprimidos),
                                   MenuItem("Abrir ImagenISO", self.abrirImagenISO),
                                   MenuItem("Abrir Programas", self.abrirProgramas),
                                   MenuItem("Abrir Otros", self.abrirContenedor)
                                   )),
            MenuItem("Ejecutar Ahora", self.actualizar),
            MenuItem("Configuración", self.configurar),
            MenuItem("Creditos", self.creditos),
            MenuItem("Salir", self.salir)
        ))

        if len(self.rutaNueva) >= 1:
            self.controlTiempo = ControlTiempo(self.icon, self.controlHilos, self.contenido["Configuracion"],
                                               self.tiempoActualizar,
                                               rutaNueva=self.rutaNueva)
        else:
            self.controlTiempo = ControlTiempo(self.icon, self.controlHilos, self.contenido["Configuracion"],
                                               self.tiempoActualizar)
    def configurar(self):
        self.icon.notify("Aun no esta completo este modulo, por favor modifica en el contendor el archivo 'Config.json'", "Error de inicio de Bloque")

    def abrirProgramas(self):
        self.abrirArchivo("Programas")

    def abrirImagenISO(self):
        self.abrirArchivo("ImagenISO")

    def abrirSonidos(self):
        self.abrirArchivo("Sonidos")

    def abrirComprimidos(self):
        self.abrirArchivo("Comprimidos")

    def abrirImagenes(self):
        self.abrirArchivo("Imagenes")

    def actualizar(self):
        self.controlTiempo.iniciar()

    def creditos(self):
        self.icon.notify("Esta aplicación fue escrita por Mau005", "Creditos: ")
        webbrowser.open("https://github.com/Mau005")

    def abrirDocumentos(self):
        self.abrirArchivo("Documentos")

    def abrirVideos(self):
        self.abrirArchivo("Video")

    def abrirContenedor(self):
        self.abrirArchivo()

    def abrirArchivo(self, carpeta=None):
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

