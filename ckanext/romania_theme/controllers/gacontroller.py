import logging
from oauth2client.service_account import ServiceAccountCredentials
from pylons import config


from ckan.plugins.toolkit import BaseController, render

class GAController(BaseController):
	def index(self):
		# The scope for the OAuth2 request.
		SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

		# The location of the key file with the key data.
		KEY_FILEPATH = config.get('romania_theme.google_analytics_token_path')

		vars = {'token': ''}
		
		if KEY_FILEPATH:
			vars = {'token' : ServiceAccountCredentials.from_json_keyfile_name(KEY_FILEPATH, SCOPE).get_access_token().access_token}
		else:
			self.logger = logging.getLogger(__name__)
			self.logger.error("there are no google analytics secrets configured")

		return render('romania_theme/ga.html', extra_vars=vars)
