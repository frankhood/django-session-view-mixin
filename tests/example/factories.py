from django_session_mixin_view.test_utils.test_app.models import Item
import factory.django


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker('word')
    description = factory.Faker('paragraph')
