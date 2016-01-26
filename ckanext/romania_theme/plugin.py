from datetime import datetime, timedelta

from sqlalchemy import event

import ckan.lib.helpers as h
import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os


def get_number_of_files():
    return model.Session.execute("select count(*) from resource where state = 'active'").first()[0]


def get_number_of_external_links():
    return model.Session.execute("select count(*) from resource where state = 'active' and url not LIKE '%data.gov.ro%'").first()[0]


class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IResourceController, inherit=True)

    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')

    def get_helpers(self):
        return {'get_number_of_files': get_number_of_files,
                'get_number_of_external_links': get_number_of_external_links}

    # IResourceController
    def before_create(self, context, resource):
        if ('upload' in resource) and (type(resource['upload']) is not unicode) and (resource['upload'].type in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/msword']):
            raise toolkit.ValidationError(['Fisierele de tip PDF, DOC sau DOCX nu sunt permise.'])

    # IMapper
    def before_update(self, mapper, connection, instance):
        if instance.state == model.State.DELETED and instance.type in ['dataset', 'resource']:
            # TODO @palcu: remove hardcoded value
            if datetime.now() - instance.metadata_created > timedelta(seconds=10):
                h.flash_error('Nu este permisa stergerea datelor la mai mult de 5 zile dupa data incarcarii, deoarece aceste date au intrat in circuitul public.')
                return EXT_STOP

    def after_update(self, mapper, connection, instance):
        pass
