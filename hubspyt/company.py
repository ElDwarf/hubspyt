# -*- coding: utf-8 -*-
from tools import Connection


class Company(object):
    """
    Permite crear/gestionar los contactos en Hubspot.

    Parametros:
        API-KEY
    """

    def __init__(self, apikey_value):
        super(Company, self).__init__()
        self.coneccion = Connection(apikey_value)
        self.id = None

    def create(self, name, description):
        """
        Metodo para crear company en la api de hubspot

        Parametros:
            name: nombre del nuevo contacto
            description: campo descriocion de la company
        """
        xurl = '/companies/v2/companies/'
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
        """
        Metodo para agregar un contacto a una company en la api de hubspot,
        este metodo se puede utilizar si se tiene cargado los datos de una
        company en la instancia (CompanyID,)

        Parametros:
            vid: del contacto
        """
        if self.id is not None:
            xurl = '/companies/v2/companies/%s/contacts/%s' % (
                self.id, vid
            )
            relation_dic = {
                "companyId": self.id,
                "vid": vid
            }
            response = self.coneccion.send_put_request(xurl, relation_dic)
            try:
                response_dic = response.json()
                self.name = response_dic['properties']['name']['value']
                self.description = response_dic['properties']['description']['value']
                self.id = response_dic['companyId']
            except:
                pass
            return response_dic
        else:
            return None
