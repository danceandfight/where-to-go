# Generated by Django 3.0.8 on 2021-01-29 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20210120_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
