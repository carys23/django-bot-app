# Generated by Django 2.2.12 on 2022-07-16 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_delete_choice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FirstQuestion',
            new_name='Question',
        ),
    ]