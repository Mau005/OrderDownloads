# OrderDownloads
Esta aplicacion esta diseñada para ordenar carpetas con mucho contenido, por ejemplo las descargas

## Requerimientos

- python 3x
- pystray~=0.19.4
- Pillow~=9.1.1

## Imagenes:
- En esta parte estara el programa

<a href="https://imgbb.com/"><img src="https://i.ibb.co/dtNB9BP/1.png" alt="1" border="0"></a>

- Estas son las opciones que tiene

<a href="https://imgbb.com/"><img src="https://i.ibb.co/pZJyM79/2.png" alt="2" border="0"></a>

- Puedes abrir directamente el contenedor de las carpetas

<a href="https://imgbb.com/"><img src="https://i.ibb.co/KW6MLGB/3.png" alt="3" border="0"></a>

- Te enviare una notificación informando que se ejecuto

<a href="https://imgbb.com/"><img src="https://i.ibb.co/8XV8CNf/4.png" alt="4" border="0"></a>

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