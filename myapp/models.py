import datetime
from django.db import models

# Create your models here.
class MyModel(models.Model):
    user = models.ForeignKey('auth.User', limit_choices_to={'last_login__lte': datetime.date.today})
