from django.db import models
from django.conf import settings

class Task(models.Model):
    class Priority(models.TextChoices):
        BAIXA = "B", "Baixa"
        MEDIA = "M", "Média"
        ALTA = "A", "Alta"
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
    titulo = models.CharField("Título", max_length=200)
    descricao = models.TextField("Descrição", max_length=200, blank=True)
    concluida = models.BooleanField("Concluída", default=False)
    prioridade = models.CharField(
        "Prioridade",
        max_length= 1,
        choices=Priority.choices,
        default=Priority.MEDIA,
        
    )
    data_limite = models.DateField("Data limite", null=True, blank=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)
    
    class Meta:
        ordering = ["concluida", "data_limite", "-prioridade", "-criado_em"]
    def __str__(self) -> str:
        return self.titulo
        