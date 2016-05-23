# -*- coding: utf-8 -*-
import json

from requests.sessions import Session


class Connection(object):
    """
    Permite crear/gestionar la conexion con Hubspot.

    Parametros:
        API-KEY
    """
    HS_API_URL = "http://api.hubapi.com"

    def __init__(self, apikey_value):
        super(Connection, self).__init__()
        self.APIKEY_VALUE = apikey_value
        self.APIKEY = "?hapikey=" + self.APIKEY_VALUE
        self.session = Session()
        self.session.headers['User-Agent'] = 'Frank Collaboration'

    def send_request(self, method, xurl, query_string_args=None, parameters=None,):
        """
        Metodo generico de comunicacion con la api de hubspot

        Parametros:
            method: metodo de comunicacion,
            xurl: url pacial de la API,
            parameters: Diccionario con los parametros para la api
        """
        url = self.HS_API_URL + xurl + self.APIKEY

        query_string_args = query_string_args or {}
        query_string_args = dict(query_string_args)

        request_headers = \
            {'content-type': 'application/json'} if parameters else {}

        if parameters:
            request_parameters = json.dumps(parameters)
        else:
            request_parameters = None

        response = self.session.request(
            method,
            url,
            params=query_string_args,
            data=request_parameters,
            headers=request_headers,
            )
        return response

    def send_get_request(self, url_path, query_string_args=None):
        """
        Metodo GET de comunicacion con la api de hubspot

        Parametros:
            url_path: url de la funcion de la api a implementar
        """
        return self.send_request('GET', url_path, query_string_args)

    def send_post_request(self, url_path, parameters):
        """
        Metodo POST de comunicacion con la api de hubspot

        Parametros:
            url_path: url de la funcion de la api a implementar
            parameters: Parametros requeridos por la funcion
        """
        return self.send_request('POST', url_path, parameters=parameters)

    def send_put_request(self, url_path, parameters):
        """
        Metodo PUT de comunicacion con la api de hubspot

        Parametros:
            url_path: url de la funcion de la api a implementar
            parameters: Parametros requeridos por la funcion
        """
        return self.send_request('PUT', url_path, parameters=parameters)
