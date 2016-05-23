# -*- coding: utf-8 -*-
from tools import Connection


class Workflow(object):
    """
    Permite obtener y agregar cotnact en workflor de Hubspot.

    Parametros:
        API-KEY
    """

    def __init__(self, apikey_value):
        super(Workflow, self).__init__()
        self.coneccion = Connection(apikey_value)
        self.id = None

    def get_all_workflow(self):
        """
        Metodo para obtener todos los workflow de la api de hubspot

        Parametros:
            N/A
        """
        xurl = '/automation/v3/workflows'
        response = self.coneccion.send_get_request(xurl)
        try:
            response_dic = response.json()
        except:
            pass
        return response_dic

    def set_workflow_id(self, id):
        self.id = id

    def add_contact(self, email_contact):
        """
        Metodo para agregar un contacto a un workflow seleccionado en la
        instancia previamente (CompanyID,)

        Parametros:
            email_contact: email del contacto a en asociar
        """
        if self.id is not None:
            xurl = '/automation/v2/workflows/%s/enrollments/contacts/%s' % (
                self.id, email_contact
            )
            relation_dic = {}
            response = self.coneccion.send_post_request(xurl, relation_dic)
            try:
                response_dic = response.json()
                return response_dic
            except:
                pass
        else:
            return None
