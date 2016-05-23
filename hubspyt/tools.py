import json

from requests.sessions import Session


class Connection(object):
    APIKEY_VALUE = "f4fb8a1a-255a-4abe-9591-8f646b63a846"
    HS_API_URL = "http://api.hubapi.com"

    def __init__(self, apikey_value):
        super(Connection, self).__init__()
        self.APIKEY_VALUE = apikey_value
        self.APIKEY = "?hapikey=" + self.APIKEY_VALUE
        self.session = Session()
        self.session.headers['User-Agent'] = 'Frank Collaboration'

    def send_request(self, method, xurl, query_string_args=None, body_deserialization=None,):
        url = self.HS_API_URL + xurl + self.APIKEY

        query_string_args = query_string_args or {}
        query_string_args = dict(query_string_args)

        request_headers = \
            {'content-type': 'application/json'} if body_deserialization else {}

        if body_deserialization:
            request_body_serialization = json.dumps(body_deserialization)
        else:
            request_body_serialization = None

        response = self.session.request(
            method,
            url,
            params=query_string_args,
            data=request_body_serialization,
            headers=request_headers,
            )
        return response

    def send_get_request(self, url_path, query_string_args=None):
        return self.send_request('GET', url_path, query_string_args)

    def send_post_request(self, url_path, body_deserialization):
        return self.send_request('POST', url_path, body_deserialization=body_deserialization)
