# Generated by Django 5.1.1 on 2024-09-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=3, max_digits=7),
        ),
    ]
