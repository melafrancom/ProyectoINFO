# ProyectoINFO 2022


## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [VISUAL_STUDIO_CODE](https://code.visualstudio.com/) - usado para codear.
* [GIT](https://git-scm.com/) - usado para guardar versiones.
* [GITHUB](https://github.com/) - usado para subir el repositorio y trabajar en equipo.
* [DJANGO](https://www.djangoproject.com/) - el framework utilizado para el desarrollo.
* [HEROKU](https://id.heroku.com/login) - utilizado para subir el proyecto.
* [TRELLO](https://trello.com/) - usado para organizarnos y trabajar en equipo.


## Autores ✒️

* **Franco Maximiliano MELA** - *Trabajo FINAL: Back-end + Front-end + deploy + coordinación.* - [melitaf](https://github.com/melitaf)
* **Santiago MARTIN** - *Trabajo FINAL: Front-end + eleboracion de textos + busqueda de imágenes.* - [zzantiago](https://github.com/zzantiago)


* **Joaquin CLEVA** - *Trabajo FINAL: Ayudo a hacer deploy* - [joaquincleva](https://github.com/joaquincleva)


También puedes mirar la lista de todos los [contribuyentes](https://github.com/melitaf/ProyectoINFO/graphs/contributors) quíenes han participado en este proyecto, y tambien a través de [TRELLO](https://trello.com/b/tHGTrbiw/fundacion-info2022) cómo nos organizamos.
------------------------------------------------------------------------------------------------------------------------


## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

_Para crear el archivo "local.py" que no se debe subir en el repositorio de git.

```
from .base import *

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'info2022fundacion',
        'USER' : 'root',
        'PASSWORD' : '>>>PONER LA CONTRASEÑA DE TU GESTOR DE BD<<<',
        'HOST' : 'localhost',
        'PORT' : '3306'
    }

}
```

### Pre-requisitos 📋

_Lo que necesitas para correr la aplicacion, es instalar los que esta dentro del archivo "requirements.txt"._


### Instalación 🔧


_Debes estar dentro del entorno virtual y y ejecutar el comando:_

```
_"pip install -r requirements.txt"_
```

_Luego irte a la carpeta principal:
```
_"...\ProyectoINFO\ProyectoINFO\src"_
```
_ Y ejecutar el comando cmd en dicha carpeta, y ahi escribir:
```
_"...\ProyectoINFO\ProyectoINFO\src py manage.py runserver"_
```
Y ya deberia estar corriendo el programa en tu computadora local.


****************************************************************************************************************



## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

****************************************************************************************************************
