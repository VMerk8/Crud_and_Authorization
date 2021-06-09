from django.db import models


class Portfolio(models.Model):
    company_name = models.CharField(max_length=250, verbose_name="Название комании")
    occupation = models.CharField(max_length=250, verbose_name="Род деятельности")
    owner = models.CharField(max_length=200, verbose_name="Владелец")
    phone = models.CharField(max_length=50, verbose_name="Номер телефона")
    email = models.EmailField(max_length=50, verbose_name="Email")
