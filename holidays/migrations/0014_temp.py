# Generated by Django 2.2.12 on 2022-07-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0013_typeholiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=100)),
            ],
        ),
    ]
