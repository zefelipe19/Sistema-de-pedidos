# Generated by Django 4.1.3 on 2022-11-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comandas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='is_editavel',
            field=models.BooleanField(default=False),
        ),
    ]