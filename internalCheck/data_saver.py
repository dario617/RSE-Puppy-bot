#coding: utf-8
import json, pymysql, datetime, time
import mysqlcredentials

def month_to_number(month):
    m = { 'ene': 1, 'jan': 1, 'feb': 2, 'mar': 3, 'abr':4, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'ago':8, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dic':12, 'dec':12 }
    return m[month]


def text_to_dict(text):
	try:
		dic = json.loads(text)
		return dic
	except ValueError:
		raise Exception("[*] Error: No se pudo parsear la información enviada")

def dic_to_data(dic):
	try:
		new_dict = {}
		new_dict['measure_time'] = "%d-%d-%d %s" % (dic['Date']['year'], month_to_number(dic['Date']['month']), dic['Date']['day'], dic['Date']['time'])
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
		new_dict['disk_use'] = dic['Disk']['usage']
		new_dict['CPU'] = dic['CPU']
		return new_dict
	except Exception:
		raise Exception("[*] Error: No se pudo reconocer la información enviada")

def data_to_sql(data):
	try:
		cnx = pymysql.connect(user=mysqlcredentials.USER, passwd=mysqlcredentials.PASS,
										host=mysqlcredentials.HOST, db=mysqlcredentials.DB, port=3306)
		table = "measurements"
		cursor = cnx.cursor()
		placeholders = ', '.join(['%s'] * len(data))
		columns = ', '.join(data.keys())
		sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table , columns, placeholders)
		cursor.execute(sql, list(data.values()))
		cnx.commit()
		cnx.close()
	except Exception as e:
		raise e
		#raise Exception("[*] Error: No se pudo guardar la información enviada")

def save_data(info):
	try:
		dic = text_to_dict(info)
		data = dic_to_data(dic)
		data_to_sql(data)
	except Exception as e:
		raise e
