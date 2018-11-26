#coding: utf-8
import os, time, sys, sender

def main(ip, port):
	while 1:
		try:
			print "\n[*] Enviando información."
			run(ip, port)
			time.sleep(5)
		except KeyboardInterrupt: #cierro servicio con ctrl+c, pero que se vea lindo
			print "\n[*] Cerrando Micro-Servicio ..."
			sys.exit(1)

def run(ip, port):
	try:
		data = os.popen("./getinfo.sh").read()
		sender.send_data(ip, port, data)
	except Exception as e:
		print e

if __name__ == "__main__":
	if len(sys.argv) < 3:
		ip = "127.0.0.1"
		port = 8081
	else:
		ip = str(sys.argv[1])
		port = int(sys.argv[2])
	print "[*] Escuchando ip %s y puerto %d" % (ip, port)
	main(ip, port)