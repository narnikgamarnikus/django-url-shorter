=====
Usage
=====

To use Django URL shorter in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'url_shorter.apps.UrlShorterConfig',
        ...
    )

Add Django URL shorter's URL patterns:

.. code-block:: python

    from url_shorter import urls as url_shorter_urls


    urlpatterns = [
        ...
        url(r'^', include(url_shorter_urls)),
        ...
    ]
