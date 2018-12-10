# RSE-Puppy-bot

Este es cachorrito bot para poder chequear estado de servidor.
Internal checker es el sistema para checkear el estado del servidor, con un sistema en dos partes: internal checker revisa el estado del servidor y lo envía a listener que guarda la información en un db mysql (requiere mysqlcredentials.py para guardar la información de la base de datos (que por motivos obvios no se comparte en este repo)).
External checker chequea si el servidor está dando el servicio esperado y manda información a través de Telegram en caso de que cambie el estado de la página revisada (requiere tokens y esas cosas que tampoco se compartan).