=====
Usage
=====

To use django postman in a project, add it to your `INSTALLED_APPS`:

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
