from pylons import config

import ckan.lib.helpers as h
import ckan.model as model
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import os
import mimetypes

from ckanext.romania_theme.logic.auth.delete import (
    romania_theme_package_delete, romania_theme_resource_delete)


def get_number_of_files():
    return model.Session.execute("select count(*) from resource where state = 'active'").first()[0]


def get_number_of_external_links():
    return model.Session.execute("select count(*) from resource where state = 'active' and url not LIKE '%data.gov.ro%'").first()[0]


def extensions_not_both_mimetype_config_list(value, flattened_data, errors, context):
    disallowed_extensions = toolkit.aslist(flattened_data[('ckanext.romania_theme.disallowed_extensions',)])
    allowed_extensions = toolkit.aslist(flattened_data[('ckanext.romania_theme.allowed_extensions',)])
   

    if disallowed_extensions and allowed_extensions:
        raise toolkit.Invalid("You can not place items both in allowed and disallowed extensions! ")
    return value


class Romania_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IResourceController, inherit=True)
    plugins.implements(plugins.IAuthFunctions)

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
            'ckanext.romania_theme.disallowed_extensions': [ignore_missing, extensions_not_both_mimetype_config_list],
            'ckanext.romania_theme.allowed_extensions': [ignore_missing],
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

        if ('upload' in resource) and (type(resource['upload']) is not unicode) \
                and not is_resource_extension_allowed:
            # If we did not do this, the URL field would contain the filename
            # and people can press finalize afterwards.
            resource['url'] = ''

            raise toolkit.ValidationError(['Fisierul are o extensie nepermisa! ' + error_message])

    # IAuthFunctions
    def get_auth_functions(self):
        return {
            'package_delete': romania_theme_package_delete,
            'resource_delete': romania_theme_resource_delete,
        }
