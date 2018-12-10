# RSE-Puppy-bot

Este es cachorrito bot para poder chequear estado de servidor. <br/>
Internal checker es el sistema para checkear el estado del servidor, con un sistema en dos partes: internal checker revisa el estado del servidor y lo envía a listener que guarda la información en un db mysql (requiere mysqlcredentials.py para guardar la información de la base de datos (que por motivos obvios no se comparte en este repo)).  <br/>

Internal Checker obtiene la siguiente informacion del servidor en el que este corriendo:
* Memoria utilizada y disponible
* Disco utilizado y disponible
* Porcentaje de CPU utilizado
* Temperatura actual y maxima de los cores
<br/>
Estos datos son guardados en una base de datos que corre dentro de un container de Docker. Ademas, el servidor de grafana esta corriendo en otro container. Los Dockerfile y archivo docker-compose se encuentran en la carpeta docker <br/>  
<br/>
External checker chequea si el servidor está dando el servicio esperado y manda información a través de Telegram en caso de que cambie el estado de la página revisada (requiere tokens y esas cosas que tampoco se compartan).
<br/>
El bot chequea que el video se encuentre disponible y que el codigo obtenido de la request sea 200.
