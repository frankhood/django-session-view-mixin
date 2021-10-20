=====
Usage
=====

To use Django Session View Mixin in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'session_view_mixin.apps.SessionViewMixinConfig',
        ...
    )

Add Django Session View Mixin's URL patterns:

.. code-block:: python

    from session_view_mixin import urls as session_view_mixin_urls


    urlpatterns = [
        ...
        url(r'^', include(session_view_mixin_urls)),
        ...
    ]
