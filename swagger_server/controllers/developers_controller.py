import connexion
import six
from swagger_server.indicepa import send_request
from swagger_server import util


def search_amministrazioni(cod_amm=None):  # noqa: E501
    """searches amministrazioni

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: pass an optional search string for looking up inventory
    :type cod_amm: str

    :rtype: object
    """
    data = {'COD_AMM': cod_amm}
    return send_request("WS05_AMM.php", data)


def search_fatturazione_elettronica(cod_amm=None):  # noqa: E501
    """cerca per codice fiscale fatturazione elettronica

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: COD_AMM
    :type cod_amm: str

    :rtype: object
    """
    data = {'COD_AMM': cod_amm}
    return send_request("WS04_SFE.php", data)


def search_fatturazione_elettronica_by_tax_code(codice_fiscale=None):  # noqa: E501
    """cerca per codice fiscale fatturazione elettronica

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param codice_fiscale: COD_FISC
    :type codice_fiscale: str

    :rtype: object
    """
    data = {'COD_FISC': codice_fiscale}
    return send_request("WS01_SFE_CF.php", data)
