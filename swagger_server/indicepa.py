"""
 WS01_SFE_CF.php
 COD_FISC
  WS02_AOO.php
 COD_AMM, COD_AOO
  WS03_OU.php
 COD_AMM
  WS04_SFE.php
 COD_AMM
  WS05_AMM.php
 COD_AMM
  WS06_OU_CODUNI.php COD_UNI_OU
  WS07_EMAIL.php
 EMAIL
  WS08_AOOC.php
 COD_AMM, COD_AOO

"""
from os.path import join
import requests
import connexion

import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def get_auth_header():
    """Lazy load authentication header. Context does not exist
        at load time.
    """
    return connexion.request.headers.get('Authorization')


def send_request(ws, data):
    indicepa_uri = "http://www.indicepa.gov.it/public-ws/"
    data.update({"AUTH_ID": get_auth_header()})
    ret = requests.post(join(indicepa_uri, ws), data=data)
    if 200 <= ret.status_code < 300:
        return parse_response(ret)
    return ret.text, ret.status_code


def parse_response(res):
    r_j = res.json()
    ret = r_j['result'] if 'result' in r_j else r_j
    err_code = ret.get('cod_err')
    if err_code >= 900:
        return res.text, 401
    elif err_code > 0:
        return res.text, 400

    return r_j, 200
