import unicodecsv
from os.path import isfile
import logging

from ckan import model
from ckan.lib.create_test_data import CreateTestData
from ckan.lib.munge import munge_title_to_name
from ckan.plugins.toolkit import CkanCommand, get_action, ValidationError


class CreateInitialDataCommand(CkanCommand):
    """
    Create initial data with an organization and user.

    paster create_initial_data
    """

    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def __init__(self, name):
        super(CreateInitialDataCommand, self).__init__(name)

    def command(self):
        self._load_config()
        self.logger = logging.getLogger(__name__)
       
        if not model.User.get('admin'):
            user=model.User(name="admin")
            user.save()
            user._set_password('admin')
            user.save()
        
        user = model.User.get('admin')
        user.sysadmin = True
        user.save()
