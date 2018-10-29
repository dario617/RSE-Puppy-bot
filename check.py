from typing import Tuple

import requests


def check_url(url: str, method: str = 'head') -> Tuple[bool,str]:
    ok: bool = False
    msg_err: str = ''

    if method is 'head':
        r = requests.head(url)
        ok = r.status_code is requests.codes.ok
        if not ok:
            msg_err = 'Error de respuesta: código {}'.format(r.status_code)

    return ok, msg_err
