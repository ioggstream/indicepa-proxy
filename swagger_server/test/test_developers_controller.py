# coding: utf-8

from __future__ import absolute_import
from os import environ
from flask import json
from six import BytesIO

from swagger_server.models.ws01_response import WS01Response  # noqa: E501
from swagger_server.models.ws02_response import WS02Response  # noqa: E501
from swagger_server.models.ws03_response import WS03Response  # noqa: E501
from swagger_server.models.ws04_response import WS04Response  # noqa: E501
from swagger_server.models.ws05_response import WS05Response  # noqa: E501
from swagger_server.models.ws06_response import WS06Response  # noqa: E501
from swagger_server.test import BaseTestCase



class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def request(self, path, method='GET', headers=None, **kwargs):
        headers = headers or {}
        headers = dict(Authorization=f'bearer {self.token}', **headers)
        return self.client.open(path, method=method, headers=headers, **kwargs)

    def setUp(self):
        self.token = environ.get('AUTH_ID', 'Replace me with a valid token')

    def test_get_amministrazione(self):
        """Test case for get_amministrazione

        searches amministrazioni
        """
        query_string = [('cod_amm', 'c_c143')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/amministrazioni',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_amministrazioni_aree_organizzative_omogenee(self):
        """Test case for search_amministrazioni_aree_organizzative_omogenee

        searches amministrazioni
        """
        query_string = [('cod_amm', 'c_h505'),
                        ('cod_aoo', '001')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/amministrazioni-aoo',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_amministrazioni_unita_organizzative(self):
        """Test case for search_amministrazioni_unita_organizzative

        searches amministrazioni
        """
        query_string = [('cod_amm', 'c_c143')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/amministrazioni-ou',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_fatturazione_elettronica(self):
        """Test case for search_fatturazione_elettronica

        cerca per codice fiscale fatturazione elettronica WS04
        """
        query_string = [('cod_amm', 'c_c143')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/fatturazione-elettronica',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_fatturazione_elettronica_by_tax_code(self):
        """Test case for search_fatturazione_elettronica_by_tax_code

        cerca per codice fiscale fatturazione elettronica WS06
        """
        query_string = [('codice_fiscale', '00121350086')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/fatturazione-elettronica-codice-fiscale',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_fatturazione_elettronica_by_ufficio(self):
        """Test case for search_fatturazione_elettronica_by_ufficio

        cerca per codice fiscale fatturazione elettronica WS06
        """
        query_string = [('codice_uni_ou', 'codice_uni_ou_example')]
        response = self.request(
            '/robipolli/indicepa/1.0.0/fatturazione-elettronica-ufficio',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
