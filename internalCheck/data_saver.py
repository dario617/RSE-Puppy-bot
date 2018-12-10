#coding: utf-8
from datetime import datetime
import json, mysql.connector
import mysqlcredentials

def text_to_dict(text):
	try:
		dic = json.loads(text)
		return dic
	except ValueError:
		raise Exception("[*] Error: No se pudo parsear la información enviada")

def dic_to_data(dic):
	try:
		new_dict = {}
		new_dict['measure_time'] = datetime.strptime(dic['date'] , '%d-%b-%Y %I:%M/%p') #day-month-year time https://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
		new_dict['timezone'] = dic['date']['timezone']
		new_dict['temp1_cur'] = dic['Temp4']['actual']
		new_dict['temp1_max'] = dic['Temp4']['max']
		new_dict['temp2_cur'] = dic['Temp7']['actual']
		new_dict['temp2_max'] = dic['Temp7']['max']
		new_dict['temp3_cur'] = dic['Temp10']['actual']
		new_dict['temp3_max'] = dic['Temp10']['max']
		new_dict['temp4_cur'] = dic['Temp13']['actual']
		new_dict['temp4_max'] = dic['Temp13']['max']
		new_dict['mem_dsp'] = dic['Memory']['disponible']
		new_dict['mem_use'] = dic['Memory']['usage']
		new_dict['dsk_dsp'] = dic['Disk']['disponible']
		new_dict['dsk_use'] = dic['Disk']['usage']
		new_dict['CPU'] = dic['CPU']
		return new_dict
	except Exception:
		raise Exception("[*] Error: No se pudo reconocer la información enviada")

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
		dic = text_to_dict(info)
		data = dic_to_data(dic)
		data_to_sql(data)
	except Exception, e:
		raise e
