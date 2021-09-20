=====
Usage
=====

To use Django-Session-Mixin-View in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_session_mixin_view.apps.DjangoSessionMixinViewConfig',
        ...
    )

Add Django-Session-Mixin-View's URL patterns:

.. code-block:: python

    from django_session_mixin_view import urls as django_session_mixin_view_urls


    urlpatterns = [
        ...
        url(r'^', include(django_session_mixin_view_urls)),
        ...
    ]
