# OrderDownloads
This application is used to be able to auto-save the downloads and it will run from time to time

## Requeriments

- python 3x


## Config
open Configuration.json
this file is designed to be able to configure everything you need to move your files between directories

"Video": is keys 
source is path move file
extencion is support for file in file
```
"Video": {
"source": "Video",
"extencion": [".mp4",".mov", ".wmv", ".avi", ".avchd", ".flv", ".f4v", ".swf", ".webm", ".html5"]
},
```

- EnMovimiento: it is used for the application to enter an infinite loop controlled by an update control

- actualizacion:  is used to determine every how many minutes it will look for the content and update the code

- source_new:it is used to search for a specific path in another place that does not contain the project, for example the downloads folder
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