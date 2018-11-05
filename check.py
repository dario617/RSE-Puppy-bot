from typing import Tuple
import requests
from bs4 import BeautifulSoup

TIMEOUT_WAIT_TIME = 1.0


def  getURL(page, source = "source src"):
	"""
    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
	start_link = page.find(source)
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1: end_quote]

	return url, end_quote

def check_url(url: str, method: str = 'get') -> Tuple[bool,str]:
	ok: bool = False
	msg_err: str = ''

	if method is 'get':
		try:
			r = requests.get(url, timeout=TIMEOUT_WAIT_TIME)
			ok = r.status_code is requests.codes.ok
			if not ok:
				msg_err = 'Error de respuesta: código {}'.format(r.status_code)
			
			# Check content on web page is ok
			page = str(BeautifulSoup(r.content))
			while True:
				url, n = getURL(page)
				page = page[n:]
				if url:
					# Check response
					print(url)
					inner_r = requests.get(url, timeout=TIMEOUT_WAIT_TIME)
					ok = inner_r.status_code is requests.codes.ok
					if not ok:
						print("NOT OK")
						msg_err = 'Pagina Ok - Error en contenido : código {}'.format(inner_r.status_code)
						break
				else:
					break

		except requests.exceptions.RequestException as e:
			msg_err = 'Error de respuesta: {}'.format(e)

	return ok, msg_err
