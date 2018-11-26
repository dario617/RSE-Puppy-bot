#coding: utf-8
import os, time, sys, socket

def main(ip, port):
	while 1:
		try:
			print "\n[*] Enviando información."
			run(ip, port)
			time.sleep(5)
		except KeyboardInterrupt: #cierro servicio con ctrl+c, pero que se vea lindo
			print "\n[*] Cerrando Micro-Servicio ..."
			sys.exit(1)


def send_data(ip, port, data):
	address = (ip, port)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(address)
		s.send(data)
		s.close()
	except socket.error:
		raise Exception("[*] Error: No se pudo conectar al socket deseado")

def run(ip, port):
	try:
		data = os.popen("./getinfo.sh").read()
		send_data(ip, port, data)
	except Exception as e:
		print e

if __name__ == "__main__":
	if isinstance(sys.argv,str):
		ip = "127.0.0.1"
		port = 8081
	else:
		ip = str(sys.argv[1])
		port = int(sys.argv[2])
	print "[*] Escuchando ip %s y puerto %d" % (ip, port)
	main(ip, port)