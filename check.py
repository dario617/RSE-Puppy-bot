from typing import Tuple
import requests
import crawler

TIMEOUT_WAIT_TIME = 1.0

def check_url(url: str, method: str = 'get') -> Tuple[bool,str]:
	ok: bool = False
	msg_err: str = ''

	if method is 'get':
		try:
			r = requests.get(url, timeout=TIMEOUT_WAIT_TIME)
			ok = r.status_code is requests.codes.ok
			if not ok:
				msg_err = 'Error de respuesta: código {}'.format(r.status_code)
			else:
				urls = crawler.getURL(r.content)
				for url in urls:
					status_ok, msg = check_url(url)
					if not status_ok:
						ok = status_ok
						msg_err = 'Error de respuesta: contenido con código {}'.format(msg)
						break
		except requests.exceptions.RequestException as e:
			msg_err = 'Error de respuesta: {}'.format(e)

	return ok, msg_err
