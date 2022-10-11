from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Jewelry(models.Model):
    name = models.CharField(verbose_name="İsim - Soyisim", max_length=50)

    price = models.PositiveSmallIntegerField(
        verbose_name="Takı Miktarı")

    jewelry_kind = models.CharField(verbose_name="Takı Türü", max_length=20)

    class Meta:
        db_table = "Takılar"

    def __str__(self):
        return self.jewelry_kind

    def get_absolute_url(self):
        return "/jewelry_app/jewelries_detail/%i" % self.id
