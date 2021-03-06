# Generated by Django 2.2.12 on 2022-07-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0018_holidayref'),
    ]

    operations = [
        migrations.AddField(
            model_name='africacountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='antarcticacountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='asiacountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='australiacountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='continent',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='europecountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='holiday',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='northamericacountries',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
        migrations.AddField(
            model_name='typeholiday',
            name='ref',
            field=models.ManyToManyField(to='holidays.HolidayRef'),
        ),
    ]
