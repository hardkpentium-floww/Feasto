# Generated by Django 2.2.2 on 2024-10-18 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feasto_core_clean_arch', '0002_auto_20241018_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_owner', to='feasto_core_clean_arch.User'),
        ),
    ]