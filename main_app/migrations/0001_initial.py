# Generated by Django 3.2.9 on 2022-01-11 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pokedex_number', models.IntegerField()),
                ('classification', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=100)),
                ('type2', models.CharField(max_length=100)),
                ('generation', models.IntegerField()),
            ],
        ),
    ]