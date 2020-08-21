from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    usuario: User = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        if not self.usuario.first_name:
            return self.usuario.username
        return self.usuario.first_name
