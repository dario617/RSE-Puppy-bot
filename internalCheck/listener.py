#coding: utf-8
import socket, sys, argparse
from thread import *

max_conn = 5
buffer_size = 4096


def main(listening_port): #levantamos el server proxy
	try:
		print "[*] Inicializando Sockets ..."
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

		#do something

		conn.close()
	except Exception, e:
		#fallo al pasar la info, no hacemos nada, seguimos escuchando
		print "[*] Error al leer la informacion entrante"
		conn.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Escucha por información en puerto recibido')
	parser.add_argument('port', metavar='PORT', type=int, help='Puerto para escuchar (default=8001)', nargs='?', default=8001)
	args = parser.parse_args()
	main(args.port)
	