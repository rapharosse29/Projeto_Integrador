from django.contrib import admin
from .models import Partida


@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "rodada_atual",
        "valor_de_mercado",
        "ultima_atualizacao",
    )
    list_filter = ("ativa", "data_inicio")
