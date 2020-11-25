from django.db import models


# Create your models here.
class Carteira(models.Model):
    def __str__(self):
        return "Carteira %s" % self.nome

    id_carteira = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)


class Ativo(models.Model):
    def __str__(self):
        return "Ativo %s" % self.nome

    CATEGORIAS = (
        ('fii', "Fundos Imobiliários"),
        ('aco', "Ações"),
        ('sto', "Stocks"),
        ('rit', "REITs"),
        ('opt', "Opções")
    )

    id_ativo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    categotia = models.CharField(max_length=3, choices=CATEGORIAS)


class Operacao(models.Model):
    def __str__(self):
        if self.acao_realizada is True:
            return f'{self.id_operacao} - Compra de {self.cotas} cotas'
        else:
            return f'{self.id_operacao} - Venda de {self.cotas} cotas'

    class Meta:
        verbose_name_plural = "operações"

    ACAO_REALIZADA = (
        (True, "Compra"),
        (False, "Venda")
    )
    id_operacao = models.AutoField(primary_key=True)
    acao_realizada = models.BooleanField(choices=ACAO_REALIZADA)
    cotas = models.IntegerField()
    lucro_ou_perda = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    data = models.DateField()
    valor_medio = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, default=0)
    cotas_totais = models.IntegerField(blank=True, null=True, default=0)
    fk_ativos_id = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    fk_carteira_id = models.ForeignKey(Carteira, on_delete=models.CASCADE)
