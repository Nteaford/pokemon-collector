# Generated by Django 3.2.9 on 2022-01-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hiddenmachine'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='hiddenmachines',
            field=models.ManyToManyField(to='main_app.HiddenMachine'),
        ),
    ]
