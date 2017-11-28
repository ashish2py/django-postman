=============================
django postman
=============================

.. image:: https://badge.fury.io/py/django-postman.svg
    :target: https://badge.fury.io/py/django-postman

.. image:: https://travis-ci.org/ashish2py/django-postman.svg?branch=master
    :target: https://travis-ci.org/ashish2py/django-postman

.. image:: https://codecov.io/gh/ashish2py/django-postman/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ashish2py/django-postman

Service for email and sms

Documentation
-------------

The full documentation is at https://django-postman.readthedocs.io.

Quickstart
----------

Install django postman::

    pip install django-postman

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'postman.apps.PostmanConfig',
        ...
    )

Add django postman's URL patterns:

.. code-block:: python

    from postman import urls as postman_urls


    urlpatterns = [
        ...
        url(r'^', include(postman_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
