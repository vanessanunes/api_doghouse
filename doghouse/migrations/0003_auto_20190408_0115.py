# Generated by Django 2.2 on 2019-04-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doghouse', '0002_animal_tipo_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='adotado',
            field=models.BooleanField(choices=[('false', 'False'), ('true', 'True')], default=False),
        ),
    ]
