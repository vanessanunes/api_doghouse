# Generated by Django 2.2 on 2021-11-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doghouse', '0004_auto_20190408_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='adotado',
            field=models.BooleanField(default=False),
        ),
    ]
