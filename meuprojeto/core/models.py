from django.db import models
from django.contrib.auth.models import User


class Partida(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="partidas")

    estado_jogo = models.JSONField(default=dict)

    rodada_atual = models.IntegerField(default=1)
    valor_de_mercado = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00
    )

    data_inicio = models.DateTimeField(auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    ativa = models.BooleanField(default=True)

    class Meta:
        ordering = ["-ultima_atualizacao"]

    def __str__(self):
        return f"Partida de {self.usuario.username} - Rodada {self.rodada_atual}"
