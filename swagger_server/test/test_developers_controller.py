# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_search_amministrazioni(self):
        """Test case for search_amministrazioni

        searches amministrazioni
        """
        query_string = [('cod_amm', 'cod_amm_example')]
        response = self.client.open(
            '/robipolli/indicepa/1.0.0/amministrazioni',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_fatturazione_elettronica(self):
        """Test case for search_fatturazione_elettronica

        cerca per codice fiscale fatturazione elettronica
        """
        query_string = [('cod_amm', 'cod_amm_example')]
        response = self.client.open(
            '/robipolli/indicepa/1.0.0/fatturazione-elettronica',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_fatturazione_elettronica_by_tax_code(self):
        """Test case for search_fatturazione_elettronica_by_tax_code

        cerca per codice fiscale fatturazione elettronica
        """
        query_string = [('codice_fiscale', 'codice_fiscale_example')]
        response = self.client.open(
            '/robipolli/indicepa/1.0.0/fatturazione-elettronica-codice-fiscale',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
