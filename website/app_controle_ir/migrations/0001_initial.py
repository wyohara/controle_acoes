# Generated by Django 3.1.3 on 2020-11-23 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ativo',
            fields=[
                ('id_ativo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=10)),
                ('categotia', models.CharField(choices=[('fii', 'Fundos Imobiliários'), ('aco', 'Ações'), ('sto', 'Stocks'), ('rit', 'REITs'), ('opt', 'Opções')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id_carteira', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id_operacao', models.AutoField(primary_key=True, serialize=False)),
                ('acao_realizada', models.BooleanField(choices=[(True, 'Compra'), (False, 'Venda')])),
                ('cotas', models.IntegerField()),
                ('lucro_ou_perda', models.DecimalField(decimal_places=3, max_digits=10)),
                ('valor', models.DecimalField(decimal_places=3, max_digits=10)),
                ('data', models.DateField()),
                ('fk_ativos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_controle_ir.ativo')),
                ('fk_carteira_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_controle_ir.carteira')),
            ],
            options={
                'verbose_name_plural': 'operações',
            },
        ),
        migrations.CreateModel(
            name='CarteiraAtivo',
            fields=[
                ('id_carteira_ativos', models.AutoField(primary_key=True, serialize=False)),
                ('valor_medio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cotas', models.IntegerField()),
                ('fk_ativos_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_controle_ir.ativo')),
                ('fk_carteira_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_controle_ir.carteira')),
            ],
        ),
    ]
