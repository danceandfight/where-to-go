# Generated by Django 3.0.8 on 2021-01-20 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20210120_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='number',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='Номер'),
        ),
    ]