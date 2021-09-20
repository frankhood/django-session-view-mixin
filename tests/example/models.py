from django.db import models

# Create your models here.
# Put your test models here
from django.db import models


# Create your models here.

class ExampleItem(models.Model):
    name = models.CharField(max_length=255)


