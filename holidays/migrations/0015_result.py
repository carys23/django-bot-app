# Generated by Django 2.2.12 on 2022-07-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0014_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ManyToManyField(to='holidays.Holiday')),
            ],
        ),
    ]