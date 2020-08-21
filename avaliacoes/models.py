from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    usuario: User = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=False)
    nota = models.DecimalField(max_digits=2, decimal_places=1)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if not self.usuario.first_name:
            return self.usuario.username
        return self.usuario.first_name
