# OrderDownloads
Esta aplicacion esta diseñada para ordenar carpetas con mucho contenido, por ejemplo las descargas

## Requerimientos

- python 3x
- pystray~=0.19.4
- Pillow~=9.1.1

## Imagenes:

https://ibb.co/RNX2n23

https://ibb.co/ZKWmFjk

https://ibb.co/VTV7QNb

https://ibb.co/GFjP6n8
## Configuración
Abre el contenedor de donde se encuentra el programa y modifica la Config.json

"Video": son las llaves 
source la carpeta donde se movera
extencion las extenciones que se agregaran
```
"Video": {
"source": "Video",
"extencion": [".mp4",".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".webm", ".html5"]
},
```

- EnMovimiento: se utiliza para que el programa corra en un bucle revisando cada cierto tiempo

- actualizacion: cantidad de minutos que requiere el programa para revisar y ordenar los archivos

- source_new: es la ruta donde quieres ir a buscar los archivos por ejemplo descargas
```
"enMovimiento": false,
"actualizacion": 1,
"source_new": "C:\\Users\\mpino\\Downloads"
```
# releases:
- https://github.com/Mau005/OrderDownloads/releases
# Channels
- https://www.youtube.com/maugame
- https://www.twitch.tv/maugameofficial