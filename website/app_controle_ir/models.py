from django.db import models


# Create your models here.
class Carteira(models.Model):
    id_carteira = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)


class Ativo(models.Model):
    CATEGORIAS = (
        ('fii', "Fundos Imobiliários"),
        ('aco', "Ações"),
        ('sto', "Stocks"),
        ('rit', "REITs"),
        ('opt', "Opções")
    )

    id_ativo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=10)
    categotia = models.CharField(max_length=3,  choices=CATEGORIAS)


class CarteiraAtivo(models.Model):
    id_carteira_ativos = models.AutoField(primary_key=True)
    valor_medio = models.DecimalField(max_digits=10, decimal_places=3)
    cotas = models.IntegerField()
    fk_carteira_id = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    fk_ativos_id = models.ForeignKey(Ativo, on_delete=models.CASCADE)


class Operacao(models.Model):
    class Meta:
        verbose_name_plural = "operações"

    ACAO_REALIZADA = (
        (True, "Compra"),
        (False, "Venda")
    )
    id_operacao = models.AutoField(primary_key=True)
    acao_realizada = models.BooleanField(choices=ACAO_REALIZADA)
    cotas = models.IntegerField()
    lucro_ou_perda = models.DecimalField(max_digits=10, decimal_places=3)
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    data = models.DateField()
    fk_ativos_id = models.ForeignKey(Ativo, on_delete=models.CASCADE)
