from django.db import models

class Visitante(models.Model):

    DESTINO = (
    ("101", "101"),
    ("201", "201"),
    ("301", "301"),
    ("401", "401"),
    ("501", "501"),
)

    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    destino = models.CharField(max_length=3, choices= DESTINO)
    data = models.DateTimeField(null=True, blank="True", )

    def __str__(self):
        return self.nome