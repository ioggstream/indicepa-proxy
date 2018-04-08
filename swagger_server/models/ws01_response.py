# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ws01_response_data import WS01ResponseData  # noqa: F401,E501
from swagger_server.models.ws05_response_result import WS05ResponseResult  # noqa: F401,E501
from swagger_server import util


class WS01Response(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: List[WS01ResponseData]=None, result: WS05ResponseResult=None):  # noqa: E501
        """WS01Response - a model defined in Swagger

        :param data: The data of this WS01Response.  # noqa: E501
        :type data: List[WS01ResponseData]
        :param result: The result of this WS01Response.  # noqa: E501
        :type result: WS05ResponseResult
        """
        self.swagger_types = {
            'data': List[WS01ResponseData],
            'result': WS05ResponseResult
        }

        self.attribute_map = {
            'data': 'data',
            'result': 'result'
        }

        self._data = data
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'WS01Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WS01Response of this WS01Response.  # noqa: E501
        :rtype: WS01Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[WS01ResponseData]:
        """Gets the data of this WS01Response.


        :return: The data of this WS01Response.
        :rtype: List[WS01ResponseData]
        """
        return self._data

    @data.setter
    def data(self, data: List[WS01ResponseData]):
        """Sets the data of this WS01Response.


        :param data: The data of this WS01Response.
        :type data: List[WS01ResponseData]
        """

        self._data = data

    @property
    def result(self) -> WS05ResponseResult:
        """Gets the result of this WS01Response.


        :return: The result of this WS01Response.
        :rtype: WS05ResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: WS05ResponseResult):
        """Sets the result of this WS01Response.


        :param result: The result of this WS01Response.
        :type result: WS05ResponseResult
        """

        self._result = result
