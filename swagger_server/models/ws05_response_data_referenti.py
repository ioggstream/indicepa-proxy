# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class WS05ResponseDataReferenti(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cogn_ref: str=None, nome_ref: str=None):  # noqa: E501
        """WS05ResponseDataReferenti - a model defined in Swagger

        :param cogn_ref: The cogn_ref of this WS05ResponseDataReferenti.  # noqa: E501
        :type cogn_ref: str
        :param nome_ref: The nome_ref of this WS05ResponseDataReferenti.  # noqa: E501
        :type nome_ref: str
        """
        self.swagger_types = {
            'cogn_ref': str,
            'nome_ref': str
        }

        self.attribute_map = {
            'cogn_ref': 'cogn_ref',
            'nome_ref': 'nome_ref'
        }

        self._cogn_ref = cogn_ref
        self._nome_ref = nome_ref

    @classmethod
    def from_dict(cls, dikt) -> 'WS05ResponseDataReferenti':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WS05Response_data_Referenti of this WS05ResponseDataReferenti.  # noqa: E501
        :rtype: WS05ResponseDataReferenti
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cogn_ref(self) -> str:
        """Gets the cogn_ref of this WS05ResponseDataReferenti.

        Cognome del referente dell'Ente  # noqa: E501

        :return: The cogn_ref of this WS05ResponseDataReferenti.
        :rtype: str
        """
        return self._cogn_ref

    @cogn_ref.setter
    def cogn_ref(self, cogn_ref: str):
        """Sets the cogn_ref of this WS05ResponseDataReferenti.

        Cognome del referente dell'Ente  # noqa: E501

        :param cogn_ref: The cogn_ref of this WS05ResponseDataReferenti.
        :type cogn_ref: str
        """

        self._cogn_ref = cogn_ref

    @property
    def nome_ref(self) -> str:
        """Gets the nome_ref of this WS05ResponseDataReferenti.

        Nome del referente dell'Ente  # noqa: E501

        :return: The nome_ref of this WS05ResponseDataReferenti.
        :rtype: str
        """
        return self._nome_ref

    @nome_ref.setter
    def nome_ref(self, nome_ref: str):
        """Sets the nome_ref of this WS05ResponseDataReferenti.

        Nome del referente dell'Ente  # noqa: E501

        :param nome_ref: The nome_ref of this WS05ResponseDataReferenti.
        :type nome_ref: str
        """

        self._nome_ref = nome_ref
