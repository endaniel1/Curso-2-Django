# Generated by Django 3.0.8 on 2020-08-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion'),
        ),
    ]