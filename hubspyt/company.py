import json
from tools import Connection

class Company(object):

    def __init__(self, apikey_value):
        super(Company, self).__init__()
        self.coneccion = Connection(apikey_value)

    def create(self, name, description):
        xurl =  '/companies/v2/companies/'
        company_dic = {
            "properties": [
                {
                    "name": "name",
                    "value": name
                },
                {
                    "name": "description",
                    "value": description
                }
            ]
        }
        response = self.coneccion.send_post_request(xurl, company_dic)
        try:
            response_dic = response.json()
            self.name = response_dic['properties']['name']['value']
            self.description = response_dic['properties']['description']['value']
            self.id = response_dic['companyId']
        except:
            pass
        return response_dic

    def add_contact(self, vid):
        xurl = '/companies/v2/companies/:companyId/contacts/:vid'
