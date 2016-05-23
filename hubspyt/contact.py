# -*- coding: utf-8 -*-
from tools import Connection


class Contact(object):
    """
    Permite crear/gestionar los contactos en Hubspot.

    Parametros:
        API-KEY
    """

    def __init__(self, apikey_value):
        super(Contact, self).__init__()
        self.coneccion = Connection(apikey_value)

    def create(self, email, data=None):
        """
        Metodo para crear contactos en la api de hubspot

        Parametros:
            email: email del nuevo contacto
            data: disccionario con datos adicionales del contacto, ej
                data = {
                    'first_name': '',
                    'last_name': '',
                    'website': '',
                    'company': '',
                    'phone': '',
                    'address': '',
                    'city': '',
                    'state': '',
                    'zip': '',
                }
        """
        xurl = '/contacts/v1/contact/createOrUpdate/email/%s' % email
        contact_dic = {
            "properties": [
                {
                    "property": "email",
                    "value": email
                },
                {
                    "property": "firstname",
                    "value": data['first_name'] if 'first_name' in data else ''
                },
                {
                    "property": "lastname",
                    "value": data['last_name'] if 'last_name' in data else ''
                },
                {
                    "property": "website",
                    "value": data['website'] if 'website' in data else ''
                },
                {
                    "property": "company",
                    "value": data['company'] if 'company' in data else ''
                },
                {
                    "property": "phone",
                    "value": data['phone'] if 'phone' in data else ''
                },
                {
                    "property": "address",
                    "value": data['address'] if 'address' in data else ''
                },
                {
                    "property": "city",
                    "value": data['city'] if 'city' in data else ''
                },
                {
                    "property": "state",
                    "value": data['state'] if 'state' in data else ''
                },
                {
                    "property": "zip",
                    "value": data['zip'] if 'zip' in data else ''
                }
            ]
        }
        response = self.coneccion.send_post_request(xurl, contact_dic)
        return response
        try:
            response_dic = response.json()
            self.email = email
            self.id = response_dic['vid']
            return response_dic
        except:
            return None
