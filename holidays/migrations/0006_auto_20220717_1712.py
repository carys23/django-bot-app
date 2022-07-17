# Generated by Django 2.2.12 on 2022-07-17 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0005_continent'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfricaCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AntarcticaCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AsiaCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AustraliaCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EuropeCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NorthAmericaCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='holiday',
            name='hoilday_ref',
        ),
        migrations.AlterField(
            model_name='continent',
            name='continents_field',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='TypeHoliday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_hol', models.CharField(max_length=100)),
                ('continent', models.ManyToManyField(to='holidays.Holiday')),
            ],
        ),
    ]
