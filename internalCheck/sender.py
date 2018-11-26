#coding: utf-8
import socket

def send_data(ip, port, data):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.send(data)
		s.close()
	except socket.error:
		raise Exception("[*] Error: No se pudo conectar al socket deseado")