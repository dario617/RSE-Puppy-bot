#coding: utf-8
import socket, sys, json, urllib
from thread import *

max_conn = 5
buffer_size = 4096


def main(listening_port): #levantamos el server proxy
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #libreria apertura socket
		print "[*] Socket bindeando ..."
		s.bind(('', listening_port)) #bindeo socket, puerto
		print "[*] Escuchando al Socket [ %d ]" % listening_port
		s.listen(max_conn) #empiezo a escuchar socket		
		print "[*] Socket inicializado!"
	except Exception, e:
		print "[*] Error al inicializar el Socket" #en caso de error, todo a las pailas
		sys.exit(2)

	while 1: #me quedo escuchando
		try:
			conn, addr = s.accept() #acepto la conexion del cliente
			start_new_thread(conn_string, (conn, addr)) #creo un thread para manejar la conexión
		except KeyboardInterrupt: #cierro proxy con ctrl+c, pero que se vea lindo
			s.close()
			print "\n[*] Cerrando Server Proxy ..."
			sys.exit(1)
	s.close()


def conn_string(conn, addr):
	try:
		request = conn.recv(buffer_size) #recibo la info
		print "[*] request:", request

		#proxy_server(url, conn)
		conn.close()
	except Exception, e:
		#fallo al pasar la info, no hacemos nada, seguimos escuchando
		print "[*] Error al leer la informacion entrante"
		conn.close()

def proxy_server(url, conn):
	try:
		data = urllib.urlopen(url)
		mime = data.info()
		reply = data.read()

		#do shit

		conn.close()

	except Exception, e:
		conn.close()
		sys.exit()


if __name__ == "__main__":
	if isinstance(sys.argv,str):
		print "[*] Inicializando Sockets [ 8081 ] ..."
		main(8081)
	else:
		print "[*] Inicializando Sockets [ %d ] ..." % int(sys.argv[1])
		main(int(sys.argv[1]))