# Generated by Django 3.2.9 on 2022-02-17 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customersupport'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
