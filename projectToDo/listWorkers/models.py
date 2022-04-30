from django.db.models import Model, CharField
# Create your models here.

class Workers(Model):
    name = CharField("name", max_length=1000)
    surname = CharField("surname", max_length=1000)

    class Meta:
        verbose_name = "Workers"
        verbose_name_plural = "Workers"

    def __str__(self):
        return f" {self.name} {self.surname} "
