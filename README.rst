=============================
Django-Session-View-Mixin
=============================

.. image:: https://badge.fury.io/py/django-session-mixin-view.svg
    :target: https://badge.fury.io/py/django-session-mixin-view

.. image:: https://travis-ci.org/yourname/django-session-mixin-view.svg?branch=master
    :target: https://travis-ci.org/yourname/django-session-mixin-view

.. image:: https://codecov.io/gh/yourname/django-session-mixin-view/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/yourname/django-session-mixin-view

pacchetto per la gestione delle sessioni

Documentation
-------------

The full documentation is at https://django-session-mixin-view.readthedocs.io.

Quickstart
----------

Install Django-Session-View-Mixin::

    pip install django-session-view-mixin

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'session_mixin_view',
        ...
    )

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


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
