# Generated by Django 2.2.2 on 2024-10-18 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feasto_core_clean_arch', '0004_auto_20241018_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
