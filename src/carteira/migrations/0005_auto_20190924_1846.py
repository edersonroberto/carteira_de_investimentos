# Generated by Django 2.2 on 2019-09-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carteira', '0004_auto_20190924_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='ticker',
            field=models.TextField(default='BID4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dividendos',
            name='ticker',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='ticker',
            field=models.TextField(),
        ),
    ]
