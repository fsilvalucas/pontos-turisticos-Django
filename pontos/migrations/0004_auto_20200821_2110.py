# Generated by Django 3.1 on 2020-08-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('pontos', '0003_auto_20200821_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='localizacao.endereco'),
        ),
    ]
