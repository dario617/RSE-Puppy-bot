#coding: utf-8
import json, mysql.connector
import mysqlcredentials

def text_to_dict(text):
	try:
		data = json.loads(text)
		return data
	except ValueError:
		raise Exception("[*] Error: No se pudo parsear la información enviada")

def data_to_sql(data):
	try:
		cnx = mysql.connector.connect(user=mysqlcredentials.USER, password=mysqlcredentials.PASS,
										host=mysqlcredentials.HOST, database=mysqlcredentials.DB)
		cursor = cnx.cursor()
		placeholders = ', '.join(['%s'] * len(data))
		columns = ', '.join(data.keys())
		sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
		cursor.execute(sql, data.values())
	except Exception:
		raise Exception("[*] Error: No se pudo guardar la información enviada")

def save_data(info):
	try:
		data = text_to_dict(info)
		data_to_sql(data)
	except Exception, e:
		raise e
