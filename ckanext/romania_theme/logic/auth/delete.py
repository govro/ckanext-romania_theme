from datetime import datetime, timedelta

from ckan.logic.auth.delete import package_delete, resource_delete

ERROR_STRING = """Nu este permisa stergerea datelor la mai mult de 5 zile dupa
    data incarcarii, deoarece aceste date au intrat in circuitul public."""


def romania_theme_package_delete(context, data_dict):
    model = context['model']
    package = model.Package.get(data_dict['id'])

    if datetime.now() - package.metadata_created > timedelta(days=5):
        return {'success': False, 'msg': ERROR_STRING}
    return package_delete(context, data_dict)


def romania_theme_resource_delete(context, data_dict):
    model = context['model']
    resource = model.Resource.get(data_dict['id'])

    if datetime.now() - resource.created > timedelta(days=5):
        return {'success': False, 'msg': ERROR_STRING}
    return resource_delete(context, data_dict)
