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

2. Install the ckanext-romania_theme Python package into your virtual environment::

     pip install ckanext-romania_theme

3. Add ``romania_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

None a the moment


------------------------
Development Installation
------------------------

To install ckanext-romania_theme for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/palcu/ckanext-romania_theme.git
    cd ckanext-romania_theme
    python setup.py develop
    pip install -r dev-requirements.txt


-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini


---------------------------------
Registering ckanext-romania_theme on PyPI
---------------------------------

ckanext-romania_theme should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-romania_theme. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


----------------------------------------
Releasing a New Version of ckanext-romania_theme
----------------------------------------

ckanext-romania_theme is availabe on PyPI as https://pypi.python.org/pypi/ckanext-romania_theme.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
