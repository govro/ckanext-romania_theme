from pylons import config

import ckan.lib.helpers as h
import ckan.model as model
from ckan.lib.plugins import DefaultTranslation
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os
from routes.mapper import SubMapper
import mimetypes

from ckanext.romania_theme.logic.auth.delete import (
    romania_theme_package_delete, romania_theme_resource_delete)


def get_number_of_files():
    return model.Session.execute("select count(*) from resource where state = 'active'").first()[0]


def get_number_of_external_links():
    return model.Session.execute("select count(*) from resource where state = 'active' and url not LIKE '%data.gov.ro%'").first()[0]


class Romania_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITranslation)

    # IRoutes
    def after_map(self, mapping):
        GA_CONTROLLER = """
            ckanext.romania_theme.controllers.gacontroller:GAController"""
        with SubMapper(mapping, controller=GA_CONTROLLER) as m:
            m.connect('ga_index',
                      '/romania_theme/ga',
                      action='index')
        return mapping
    # IConfigurer
    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'romania_theme')

    def get_helpers(self):
        return {'get_number_of_files': get_number_of_files,
                'get_number_of_external_links': get_number_of_external_links}

    def update_config_schema(self, schema):
        ignore_missing = toolkit.get_validator('ignore_missing')

        schema.update({
            'ckanext.romania_theme.disallowed_extensions': [ignore_missing, unicode],
            'ckanext.romania_theme.allowed_extensions': [ignore_missing, unicode],
        })

        return schema

    # IResourceController
    def before_create(self, context, resource):
        disallowed_extensions = toolkit.aslist(config.get('ckanext.romania_theme.disallowed_extensions',[]))
        disallowed_mimetypes = [mimetypes.types_map["." + x] for x in disallowed_extensions]

        allowed_extensions = toolkit.aslist(config.get('ckanext.romania_theme.allowed_extensions',[]))
        allowed_mimetypes = [mimetypes.types_map["." + x] for x in allowed_extensions]

        is_resource_extension_allowed = False
        error_message = ''
        if (type(resource['upload']) is not unicode):
            if allowed_mimetypes:
                if resource['upload'].type in allowed_mimetypes:
                    is_resource_extension_allowed = True
                else:
                    error_message="Doar urmatoarele extensii sunt permise: " + ", ".join(allowed_extensions) + "."
            else:
                if resource['upload'].type not in disallowed_mimetypes:
                    is_resource_extension_allowed = True
                else:
                    error_message= "Urmatoarele extensii sunt nepermise: " + ", ".join(disallowed_extensions) + "."

        if ('upload' in resource) and (type(resource['upload']) is not unicode) and not is_resource_extension_allowed:
            # If we did not do this, the URL field would contain the filename
            # and people can press finalize afterwards.
            resource['url'] = ''

            raise toolkit.ValidationError(['Fisierul are o extensie nepermisa! ' + error_message])

    def before_show(context, resource_dict):
        custom_url = config.get('romania_theme.custom_resource_download_url')

        if custom_url:
            # We should probably treat this exception. But let it fail here. You should add ckan.site_url to the config
            old_url = config['ckan.site_url']
            resource_dict['romania_download_url'] = resource_dict['url'].replace(old_url, custom_url)
        else:
            resource_dict['romania_download_url'] = resource_dict['url']
        return resource_dict

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            'package_delete': romania_theme_package_delete,
            'resource_delete': romania_theme_resource_delete,
        }
