# Generated by Django 2.2.2 on 2024-10-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feasto_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'UNAVAILABLE')], default='AVAILABLE', max_length=30),
        ),
    ]