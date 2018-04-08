# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.ws05_response_result import WS05ResponseResult  # noqa: F401,E501
from swagger_server.models.ws06_response_data import WS06ResponseData  # noqa: F401,E501
from swagger_server import util


class WS06Response(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, data: WS06ResponseData=None, result: WS05ResponseResult=None):  # noqa: E501
        """WS06Response - a model defined in Swagger

        :param data: The data of this WS06Response.  # noqa: E501
        :type data: WS06ResponseData
        :param result: The result of this WS06Response.  # noqa: E501
        :type result: WS05ResponseResult
        """
        self.swagger_types = {
            'data': WS06ResponseData,
            'result': WS05ResponseResult
        }

        self.attribute_map = {
            'data': 'data',
            'result': 'result'
        }

        self._data = data
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'WS06Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The WS06Response of this WS06Response.  # noqa: E501
        :rtype: WS06Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> WS06ResponseData:
        """Gets the data of this WS06Response.


        :return: The data of this WS06Response.
        :rtype: WS06ResponseData
        """
        return self._data

    @data.setter
    def data(self, data: WS06ResponseData):
        """Sets the data of this WS06Response.


        :param data: The data of this WS06Response.
        :type data: WS06ResponseData
        """

        self._data = data

    @property
    def result(self) -> WS05ResponseResult:
        """Gets the result of this WS06Response.


        :return: The result of this WS06Response.
        :rtype: WS05ResponseResult
        """
        return self._result

    @result.setter
    def result(self, result: WS05ResponseResult):
        """Sets the result of this WS06Response.


        :param result: The result of this WS06Response.
        :type result: WS05ResponseResult
        """

        self._result = result
