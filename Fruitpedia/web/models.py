from django.db import models
from django.core.validators import MinLengthValidator

from Fruitpedia.web.validators import validate_name_starts_with_letter, \
                                        validate_fruit_name_letters_only


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=[validate_name_starts_with_letter])
    last_name = models.CharField(max_length=35, validators=[validate_name_starts_with_letter])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=[MinLengthValidator(8)])
    image_url = models.URLField(blank=True)
    age = models.IntegerField(default=18, null=True)


class Fruit(models.Model):
    name = models.CharField(max_length=30, validators=[validate_fruit_name_letters_only])
    image_url = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(blank=True)
