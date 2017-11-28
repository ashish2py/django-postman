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


Quickstart
----------

Install django postman::

    pip install git+https://github.com/ashish2py/django-postman

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'postman',
        ...
    )

Change your `settings.py`:

.. code-block:: python

    # POSTMAIL_EMAILER
    EMAIL_BACKEND = 'postman.email_service.EmailBackend'
    
    # TEST Server http://testing.postman.zaya.in
    POSTMAN_HOST = '<zaya-postman-service-hostname>'
    POSTMAN_EMAIL_ROUTE = '/api/v1/services/email/'
    POSTMAN_SMS_ROUTE = '/api/v1/services/email/'
    POSTMAN_AUTHKEY = '<your-postman-auth-key>' 

How to use EmailBackend:

.. code-block:: python

    from django.core.mail import send_mail
    
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

How to use SMSBackend:

.. code-block:: python

    from postman import sms_backend
    sms_backend.send_messages(<PHONE_NUMBER>, <MESSAGE>)
    
    # PHONE_NUMBER : accepts <country_code>
    
    Optional Parameters
    # SENDER : SMSProvider's SENDER_ID
    # ROUTER : PROMOTIONAL or TRANSACTIONAL
    
    sms_backend.send_messages(<PHONE_NUMBER>, <MESSAGE>, <SENDER_ID>, <ROUTER>)
    
Features
--------

* overrides django's send_mail and uses zaya's POSTMAN service to send email
* use POSTMAN for send messages

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
