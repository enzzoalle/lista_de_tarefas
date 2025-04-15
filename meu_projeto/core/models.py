from django.db import models
from django.contrib.auth.models import User

class Materia(models.Model):
    # Matérias da faculdade
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Devolve uma representação em string do modelo
        return self.text
    
class Comentario(models.Model):
    # Comentários da matéria
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "comentarios"

    def __str__(self):
        # Devolve uma representação em string do modelo
        return self.text[:50] + "..."