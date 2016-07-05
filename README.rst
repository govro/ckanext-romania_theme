=============
ckanext-romania_theme
=============

.. image:: https://travis-ci.org/govro/ckanext-romania_theme.svg?branch=master
    :target: https://travis-ci.org/govro/ckanext-romania_theme

This extensions includes custom modifications that have been made to
http://data.gov.ro/ to support our own use cases.

------------
Requirements
------------

Built for http://github.com/datagovro/ckan version.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-romania_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Clone and install the ckanext-romania_theme Python package into your virtual environment::

     python setup.py develop

3. Add ``romania_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

```
romania_theme.custom_resource_download_url = http://data.gv.ro
romania_theme.google_analytics_token_path = /etc/ckan/default/google-analytics-secrets.json
```

-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini
