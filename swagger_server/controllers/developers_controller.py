import connexion
import six
from swagger_server.indicepa import send_request
from swagger_server import util


def get_amministrazione(cod_amm):  # noqa: E501
    """searches amministrazioni

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: COD_AMM
    :type cod_amm: str

    :rtype: WS05Response
    """
    data = {'COD_AMM': cod_amm}
    return send_request("WS05_AMM.php", data)


def search_amministrazioni_aree_organizzative_omogenee(cod_amm, cod_aoo=None):  # noqa: E501
    """searches amministrazioni

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: COD_AMM
    :type cod_amm: str
    :param cod_aoo: pass an optional search string for looking up inventory
    :type cod_aoo: str

    :rtype: WS02Response
    """
    data = {'COD_AMM': cod_amm}
    if cod_aoo is not None:
        data['COD_AOO'] = cod_aoo
    return send_request("WS02_AOO.php", data)


def search_amministrazioni_unita_organizzative(cod_amm):  # noqa: E501
    """searches amministrazioni

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: COD_AMM
    :type cod_amm: str

    :rtype: WS03Response
    """
    data = {'COD_AMM': cod_amm}
    return send_request("WS03_OU.php", data)


def search_fatturazione_elettronica(cod_amm):  # noqa: E501
    """cerca per codice fiscale fatturazione elettronica WS04

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param cod_amm: COD_AMM
    :type cod_amm: str

    :rtype: WS04Response
    """
    data = {'COD_AMM': cod_amm}
    return send_request("WS04_SFE.php", data)


def search_fatturazione_elettronica_by_tax_code(codice_fiscale):  # noqa: E501
    """cerca per codice fiscale fatturazione elettronica WS01

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param codice_fiscale: CF
    :type codice_fiscale: str

    :rtype: WS01Response
    """
    data = {'CF': codice_fiscale}
    return send_request("WS01_SFE_CF.php", data)


def search_fatturazione_elettronica_by_ufficio(codice_uni_ou):  # noqa: E501
    """cerca per codice fiscale fatturazione elettronica WS06

    By passing in the appropriate options, you can search for available inventory in the system  # noqa: E501

    :param codice_uni_ou: COD_UNI_OU
    :type codice_uni_ou: str

    :rtype: WS06Response
    """
    return 'do some magic!'
