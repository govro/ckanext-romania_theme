import webtest
import paste.fixture
import pylons.test

from ckan.tests import factories
import ckan.model as model
import ckan.config
import ckan.plugins
from routes import url_for
from ckan.tests import factories, helpers


class TestRomaniaTheme(helpers.FunctionalTestBase):
    @classmethod
    def setup_class(cls):
        cls.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        ckan.plugins.load('romania_theme')

    def setup(self):
        super(TestRomaniaTheme, self).setup()
        self.user = factories.User()
        self.user_env = {'REMOTE_USER': self.user['name'].encode('ascii')}

    def teardown(self):
        model.repo.rebuild_db()

    @classmethod
    def teardown_class(cls):
        ckan.plugins.unload('romania_theme')

    def test_motto(self):
        response = self.app.get('/')
        motto = 'Date accesibile, reutilizabile, ce pot fi redistribuite'
        assert motto in response.body

    def test_maintainer_email_not_exists(self):
        response = self.app.get(url=url_for(controller='package',
                                            action='new'))
        field_text="field-maintainer-email"
        assert field_text not in response.body

    def test_no_source_url_field_in_add_dataset_form(self):
        response = self.app.get(url = url_for(controller='package',
                                              action='new'))
        field = 'id="field-url"'
        assert field not in response.body
