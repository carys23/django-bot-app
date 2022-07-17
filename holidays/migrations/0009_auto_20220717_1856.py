# Generated by Django 2.2.12 on 2022-07-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0008_auto_20220717_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='antarcticacountries',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='asiacountries',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='australiacountries',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='europecountries',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='northamericacountries',
            name='continent',
        ),
        migrations.RemoveField(
            model_name='temp',
            name='holiday',
        ),
        migrations.RemoveField(
            model_name='typeholiday',
            name='holiday_details',
        ),
        migrations.AddField(
            model_name='holiday',
            name='continents_field',
            field=models.CharField(default='testing', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AfricaCountries',
        ),
        migrations.DeleteModel(
            name='AntarcticaCountries',
        ),
        migrations.DeleteModel(
            name='AsiaCountries',
        ),
        migrations.DeleteModel(
            name='AustraliaCountries',
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
        migrations.DeleteModel(
            name='EuropeCountries',
        ),
        migrations.DeleteModel(
            name='NorthAmericaCountries',
        ),
        migrations.DeleteModel(
            name='Temp',
        ),
        migrations.DeleteModel(
            name='TypeHoliday',
        ),
    ]