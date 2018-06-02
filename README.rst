=============================
Django URL shorter
=============================

.. image:: https://badge.fury.io/py/django-url-shorter.svg
    :target: https://badge.fury.io/py/django-url-shorter

.. image:: https://travis-ci.org/narnikgamarnikus/django-url-shorter.svg?branch=master
    :target: https://travis-ci.org/narnikgamarnikus/django-url-shorter

.. image:: https://codecov.io/gh/narnikgamarnikus/django-url-shorter/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narnikgamarnikus/django-url-shorter

Django app for shortening urls

Documentation
-------------

The full documentation is at https://django-url-shorter.readthedocs.io.

Quickstart
----------

Install Django URL shorter::

    pip install django-url-shorter

Add it to your `INSTALLED_APPS`:

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
