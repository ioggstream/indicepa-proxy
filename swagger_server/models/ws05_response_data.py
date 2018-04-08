# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ws05_response_data_referenti import WS05ResponseDataReferenti  # noqa: F401,E501
from swagger_server import util


class WS05ResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, referenti: List[WS05ResponseDataReferenti]=None, acronimo: str=None, cap: str=None, categoria: str=None, cf: str=None, cod_amm: str=None, cogn_resp: str=None, comune: str=None, data_accreditamento: str=None, des_amm: str=None, indirizzo: str=None, liv_accessibili: float=None, mail1: str=None, mail2: str=None, mail3: str=None, mail4: str=None, mail5: str=None, nome_resp: str=None, provincia: str=None, regione: str=None, sito_istituzionale: str=None, tipologia: str=None, titolo_resp: str=None):  # noqa: E501
        """WS05ResponseData - a model defined in Swagger

        :param referenti: The referenti of this WS05ResponseData.  # noqa: E501
        :type referenti: List[WS05ResponseDataReferenti]
        :param acronimo: The acronimo of this WS05ResponseData.  # noqa: E501
        :type acronimo: str
        :param cap: The cap of this WS05ResponseData.  # noqa: E501
        :type cap: str
        :param categoria: The categoria of this WS05ResponseData.  # noqa: E501
        :type categoria: str
        :param cf: The cf of this WS05ResponseData.  # noqa: E501
        :type cf: str
        :param cod_amm: The cod_amm of this WS05ResponseData.  # noqa: E501
        :type cod_amm: str
        :param cogn_resp: The cogn_resp of this WS05ResponseData.  # noqa: E501
        :type cogn_resp: str
        :param comune: The comune of this WS05ResponseData.  # noqa: E501
        :type comune: str
        :param data_accreditamento: The data_accreditamento of this WS05ResponseData.  # noqa: E501
        :type data_accreditamento: str
        :param des_amm: The des_amm of this WS05ResponseData.  # noqa: E501
        :type des_amm: str
        :param indirizzo: The indirizzo of this WS05ResponseData.  # noqa: E501
        :type indirizzo: str
        :param liv_accessibili: The liv_accessibili of this WS05ResponseData.  # noqa: E501
        :type liv_accessibili: float
        :param mail1: The mail1 of this WS05ResponseData.  # noqa: E501
        :type mail1: str
        :param mail2: The mail2 of this WS05ResponseData.  # noqa: E501
        :type mail2: str
        :param mail3: The mail3 of this WS05ResponseData.  # noqa: E501
        :type mail3: str
        :param mail4: The mail4 of this WS05ResponseData.  # noqa: E501
        :type mail4: str
        :param mail5: The mail5 of this WS05ResponseData.  # noqa: E501
        :type mail5: str
        :param nome_resp: The nome_resp of this WS05ResponseData.  # noqa: E501
        :type nome_resp: str
        :param provincia: The provincia of this WS05ResponseData.  # noqa: E501
        :type provincia: str
        :param regione: The regione of this WS05ResponseData.  # noqa: E501
        :type regione: str
        :param sito_istituzionale: The sito_istituzionale of this WS05ResponseData.  # noqa: E501
        :type sito_istituzionale: str
        :param tipologia: The tipologia of this WS05ResponseData.  # noqa: E501
        :type tipologia: str
        :param titolo_resp: The titolo_resp of this WS05ResponseData.  # noqa: E501
        :type titolo_resp: str
        """
        self.swagger_types = {
            'referenti': List[WS05ResponseDataReferenti],
            'acronimo': str,
            'cap': str,
            'categoria': str,
            'cf': str,
            'cod_amm': str,
            'cogn_resp': str,
            'comune': str,
            'data_accreditamento': str,
            'des_amm': str,
            'indirizzo': str,
            'liv_accessibili': float,
            'mail1': str,
            'mail2': str,
            'mail3': str,
            'mail4': str,
            'mail5': str,
            'nome_resp': str,
            'provincia': str,
            'regione': str,
            'sito_istituzionale': str,
            'tipologia': str,
            'titolo_resp': str
        }

        self.attribute_map = {
            'referenti': 'Referenti',
            'acronimo': 'acronimo',
            'cap': 'cap',
            'categoria': 'categoria',
            'cf': 'cf',
            'cod_amm': 'cod_amm',
            'cogn_resp': 'cogn_resp',
            'comune': 'comune',
            'data_accreditamento': 'data_accreditamento',
            'des_amm': 'des_amm',
            'indirizzo': 'indirizzo',
            'liv_accessibili': 'liv_accessibili',
            'mail1': 'mail1',
            'mail2': 'mail2',
            'mail3': 'mail3',
            'mail4': 'mail4',
            'mail5': 'mail5',
            'nome_resp': 'nome_resp',
            'provincia': 'provincia',
            'regione': 'regione',
            'sito_istituzionale': 'sito_istituzionale',
            'tipologia': 'tipologia',
            'titolo_resp': 'titolo_resp'
        }

        self._referenti = referenti
        self._acronimo = acronimo
        self._cap = cap
        self._categoria = categoria
        self._cf = cf
        self._cod_amm = cod_amm
        self._cogn_resp = cogn_resp
        self._comune = comune
        self._data_accreditamento = data_accreditamento
        self._des_amm = des_amm
        self._indirizzo = indirizzo
        self._liv_accessibili = liv_accessibili
        self._mail1 = mail1
        self._mail2 = mail2
        self._mail3 = mail3
        self._mail4 = mail4
        self._mail5 = mail5
        self._nome_resp = nome_resp
        self._provincia = provincia
        self._regione = regione
        self._sito_istituzionale = sito_istituzionale
        self._tipologia = tipologia
        self._titolo_resp = titolo_resp

    @classmethod
    def from_dict(cls, dikt) -> 'WS05ResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WS05Response_data of this WS05ResponseData.  # noqa: E501
        :rtype: WS05ResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def referenti(self) -> List[WS05ResponseDataReferenti]:
        """Gets the referenti of this WS05ResponseData.


        :return: The referenti of this WS05ResponseData.
        :rtype: List[WS05ResponseDataReferenti]
        """
        return self._referenti

    @referenti.setter
    def referenti(self, referenti: List[WS05ResponseDataReferenti]):
        """Sets the referenti of this WS05ResponseData.


        :param referenti: The referenti of this WS05ResponseData.
        :type referenti: List[WS05ResponseDataReferenti]
        """

        self._referenti = referenti

    @property
    def acronimo(self) -> str:
        """Gets the acronimo of this WS05ResponseData.

        Acronimo dell'Ente  # noqa: E501

        :return: The acronimo of this WS05ResponseData.
        :rtype: str
        """
        return self._acronimo

    @acronimo.setter
    def acronimo(self, acronimo: str):
        """Sets the acronimo of this WS05ResponseData.

        Acronimo dell'Ente  # noqa: E501

        :param acronimo: The acronimo of this WS05ResponseData.
        :type acronimo: str
        """

        self._acronimo = acronimo

    @property
    def cap(self) -> str:
        """Gets the cap of this WS05ResponseData.

        Cap registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :return: The cap of this WS05ResponseData.
        :rtype: str
        """
        return self._cap

    @cap.setter
    def cap(self, cap: str):
        """Sets the cap of this WS05ResponseData.

        Cap registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :param cap: The cap of this WS05ResponseData.
        :type cap: str
        """

        self._cap = cap

    @property
    def categoria(self) -> str:
        """Gets the categoria of this WS05ResponseData.

        Categoria dell'Ente in IPA  # noqa: E501

        :return: The categoria of this WS05ResponseData.
        :rtype: str
        """
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: str):
        """Sets the categoria of this WS05ResponseData.

        Categoria dell'Ente in IPA  # noqa: E501

        :param categoria: The categoria of this WS05ResponseData.
        :type categoria: str
        """

        self._categoria = categoria

    @property
    def cf(self) -> str:
        """Gets the cf of this WS05ResponseData.

        Codice fiscale dell'Ente  # noqa: E501

        :return: The cf of this WS05ResponseData.
        :rtype: str
        """
        return self._cf

    @cf.setter
    def cf(self, cf: str):
        """Sets the cf of this WS05ResponseData.

        Codice fiscale dell'Ente  # noqa: E501

        :param cf: The cf of this WS05ResponseData.
        :type cf: str
        """

        self._cf = cf

    @property
    def cod_amm(self) -> str:
        """Gets the cod_amm of this WS05ResponseData.

        Codice Ente accreditato in IPA  # noqa: E501

        :return: The cod_amm of this WS05ResponseData.
        :rtype: str
        """
        return self._cod_amm

    @cod_amm.setter
    def cod_amm(self, cod_amm: str):
        """Sets the cod_amm of this WS05ResponseData.

        Codice Ente accreditato in IPA  # noqa: E501

        :param cod_amm: The cod_amm of this WS05ResponseData.
        :type cod_amm: str
        """

        self._cod_amm = cod_amm

    @property
    def cogn_resp(self) -> str:
        """Gets the cogn_resp of this WS05ResponseData.

        Cognome del responsabile dell'Ente  # noqa: E501

        :return: The cogn_resp of this WS05ResponseData.
        :rtype: str
        """
        return self._cogn_resp

    @cogn_resp.setter
    def cogn_resp(self, cogn_resp: str):
        """Sets the cogn_resp of this WS05ResponseData.

        Cognome del responsabile dell'Ente  # noqa: E501

        :param cogn_resp: The cogn_resp of this WS05ResponseData.
        :type cogn_resp: str
        """

        self._cogn_resp = cogn_resp

    @property
    def comune(self) -> str:
        """Gets the comune of this WS05ResponseData.

        Comune registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :return: The comune of this WS05ResponseData.
        :rtype: str
        """
        return self._comune

    @comune.setter
    def comune(self, comune: str):
        """Sets the comune of this WS05ResponseData.

        Comune registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :param comune: The comune of this WS05ResponseData.
        :type comune: str
        """

        self._comune = comune

    @property
    def data_accreditamento(self) -> str:
        """Gets the data_accreditamento of this WS05ResponseData.

        Data di accreditamento dell'Ente  # noqa: E501

        :return: The data_accreditamento of this WS05ResponseData.
        :rtype: str
        """
        return self._data_accreditamento

    @data_accreditamento.setter
    def data_accreditamento(self, data_accreditamento: str):
        """Sets the data_accreditamento of this WS05ResponseData.

        Data di accreditamento dell'Ente  # noqa: E501

        :param data_accreditamento: The data_accreditamento of this WS05ResponseData.
        :type data_accreditamento: str
        """

        self._data_accreditamento = data_accreditamento

    @property
    def des_amm(self) -> str:
        """Gets the des_amm of this WS05ResponseData.

        Denominazione Ente accreditato in IPA  # noqa: E501

        :return: The des_amm of this WS05ResponseData.
        :rtype: str
        """
        return self._des_amm

    @des_amm.setter
    def des_amm(self, des_amm: str):
        """Sets the des_amm of this WS05ResponseData.

        Denominazione Ente accreditato in IPA  # noqa: E501

        :param des_amm: The des_amm of this WS05ResponseData.
        :type des_amm: str
        """

        self._des_amm = des_amm

    @property
    def indirizzo(self) -> str:
        """Gets the indirizzo of this WS05ResponseData.

        Indirizzo postale registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :return: The indirizzo of this WS05ResponseData.
        :rtype: str
        """
        return self._indirizzo

    @indirizzo.setter
    def indirizzo(self, indirizzo: str):
        """Sets the indirizzo of this WS05ResponseData.

        Indirizzo postale registrato in IPA per la sede legale dell'Ente  # noqa: E501

        :param indirizzo: The indirizzo of this WS05ResponseData.
        :type indirizzo: str
        """

        self._indirizzo = indirizzo

    @property
    def liv_accessibili(self) -> float:
        """Gets the liv_accessibili of this WS05ResponseData.

        livello di accessibilità del sito dell'Ente  # noqa: E501

        :return: The liv_accessibili of this WS05ResponseData.
        :rtype: float
        """
        return self._liv_accessibili

    @liv_accessibili.setter
    def liv_accessibili(self, liv_accessibili: float):
        """Sets the liv_accessibili of this WS05ResponseData.

        livello di accessibilità del sito dell'Ente  # noqa: E501

        :param liv_accessibili: The liv_accessibili of this WS05ResponseData.
        :type liv_accessibili: float
        """

        self._liv_accessibili = liv_accessibili

    @property
    def mail1(self) -> str:
        """Gets the mail1 of this WS05ResponseData.

        Indirizzo email primario associato all’Ente di tipo PEC|CECPAC  # noqa: E501

        :return: The mail1 of this WS05ResponseData.
        :rtype: str
        """
        return self._mail1

    @mail1.setter
    def mail1(self, mail1: str):
        """Sets the mail1 of this WS05ResponseData.

        Indirizzo email primario associato all’Ente di tipo PEC|CECPAC  # noqa: E501

        :param mail1: The mail1 of this WS05ResponseData.
        :type mail1: str
        """

        self._mail1 = mail1

    @property
    def mail2(self) -> str:
        """Gets the mail2 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :return: The mail2 of this WS05ResponseData.
        :rtype: str
        """
        return self._mail2

    @mail2.setter
    def mail2(self, mail2: str):
        """Sets the mail2 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :param mail2: The mail2 of this WS05ResponseData.
        :type mail2: str
        """

        self._mail2 = mail2

    @property
    def mail3(self) -> str:
        """Gets the mail3 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :return: The mail3 of this WS05ResponseData.
        :rtype: str
        """
        return self._mail3

    @mail3.setter
    def mail3(self, mail3: str):
        """Sets the mail3 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :param mail3: The mail3 of this WS05ResponseData.
        :type mail3: str
        """

        self._mail3 = mail3

    @property
    def mail4(self) -> str:
        """Gets the mail4 of this WS05ResponseData.

        Indirizzo email primario associato all’Ente  # noqa: E501

        :return: The mail4 of this WS05ResponseData.
        :rtype: str
        """
        return self._mail4

    @mail4.setter
    def mail4(self, mail4: str):
        """Sets the mail4 of this WS05ResponseData.

        Indirizzo email primario associato all’Ente  # noqa: E501

        :param mail4: The mail4 of this WS05ResponseData.
        :type mail4: str
        """

        self._mail4 = mail4

    @property
    def mail5(self) -> str:
        """Gets the mail5 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :return: The mail5 of this WS05ResponseData.
        :rtype: str
        """
        return self._mail5

    @mail5.setter
    def mail5(self, mail5: str):
        """Sets the mail5 of this WS05ResponseData.

        Indirizzo email associato all’Ente  # noqa: E501

        :param mail5: The mail5 of this WS05ResponseData.
        :type mail5: str
        """

        self._mail5 = mail5

    @property
    def nome_resp(self) -> str:
        """Gets the nome_resp of this WS05ResponseData.

        Nome del responsabile dell'Ente  # noqa: E501

        :return: The nome_resp of this WS05ResponseData.
        :rtype: str
        """
        return self._nome_resp

    @nome_resp.setter
    def nome_resp(self, nome_resp: str):
        """Sets the nome_resp of this WS05ResponseData.

        Nome del responsabile dell'Ente  # noqa: E501

        :param nome_resp: The nome_resp of this WS05ResponseData.
        :type nome_resp: str
        """

        self._nome_resp = nome_resp

    @property
    def provincia(self) -> str:
        """Gets the provincia of this WS05ResponseData.

        Provincia registrata in IPA per la sede legale dell'Ente  # noqa: E501

        :return: The provincia of this WS05ResponseData.
        :rtype: str
        """
        return self._provincia

    @provincia.setter
    def provincia(self, provincia: str):
        """Sets the provincia of this WS05ResponseData.

        Provincia registrata in IPA per la sede legale dell'Ente  # noqa: E501

        :param provincia: The provincia of this WS05ResponseData.
        :type provincia: str
        """

        self._provincia = provincia

    @property
    def regione(self) -> str:
        """Gets the regione of this WS05ResponseData.

        Regione registrata in IPA per la sede legale dell'Ente  # noqa: E501

        :return: The regione of this WS05ResponseData.
        :rtype: str
        """
        return self._regione

    @regione.setter
    def regione(self, regione: str):
        """Sets the regione of this WS05ResponseData.

        Regione registrata in IPA per la sede legale dell'Ente  # noqa: E501

        :param regione: The regione of this WS05ResponseData.
        :type regione: str
        """

        self._regione = regione

    @property
    def sito_istituzionale(self) -> str:
        """Gets the sito_istituzionale of this WS05ResponseData.

        Sito istituzionale dell'Ente  # noqa: E501

        :return: The sito_istituzionale of this WS05ResponseData.
        :rtype: str
        """
        return self._sito_istituzionale

    @sito_istituzionale.setter
    def sito_istituzionale(self, sito_istituzionale: str):
        """Sets the sito_istituzionale of this WS05ResponseData.

        Sito istituzionale dell'Ente  # noqa: E501

        :param sito_istituzionale: The sito_istituzionale of this WS05ResponseData.
        :type sito_istituzionale: str
        """

        self._sito_istituzionale = sito_istituzionale

    @property
    def tipologia(self) -> str:
        """Gets the tipologia of this WS05ResponseData.

        Tipologia dell’Ente in IPA  # noqa: E501

        :return: The tipologia of this WS05ResponseData.
        :rtype: str
        """
        return self._tipologia

    @tipologia.setter
    def tipologia(self, tipologia: str):
        """Sets the tipologia of this WS05ResponseData.

        Tipologia dell’Ente in IPA  # noqa: E501

        :param tipologia: The tipologia of this WS05ResponseData.
        :type tipologia: str
        """

        self._tipologia = tipologia

    @property
    def titolo_resp(self) -> str:
        """Gets the titolo_resp of this WS05ResponseData.

        Titolo del responsabile dell'Ente  # noqa: E501

        :return: The titolo_resp of this WS05ResponseData.
        :rtype: str
        """
        return self._titolo_resp

    @titolo_resp.setter
    def titolo_resp(self, titolo_resp: str):
        """Sets the titolo_resp of this WS05ResponseData.

        Titolo del responsabile dell'Ente  # noqa: E501

        :param titolo_resp: The titolo_resp of this WS05ResponseData.
        :type titolo_resp: str
        """

        self._titolo_resp = titolo_resp
