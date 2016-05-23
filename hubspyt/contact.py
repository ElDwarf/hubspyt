import json
from tools import Connection

class Contact(object):

    def __init__(self, apikey_value):
        super(Contact, self).__init__()
        self.coneccion = Connection(apikey_value)

    def create(self, email, data=None):
        xurl =  '/contacts/v1/contact/createOrUpdate/email/%s' % email
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
            self.name = response_dic['properties']['name']['value']
            self.description = response_dic['properties']['description']['value']
            self.id = response_dic['companyId']
        except:
            pass
        return response_dic
