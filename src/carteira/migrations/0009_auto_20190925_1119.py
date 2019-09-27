# Generated by Django 2.2 on 2019-09-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0008_auto_20190924_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteira',
            name='tipo',
            field=models.TextField(default='Ação'),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='ticker',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='dividendos',
            name='dataDividendo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dividendos',
            name='dataPagamento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='dividendos',
            name='dividendos',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='taxa',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='valorCompra',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='valorVenda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
