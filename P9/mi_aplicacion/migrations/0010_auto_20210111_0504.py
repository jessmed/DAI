# Generated by Django 3.1.5 on 2021-01-11 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0009_auto_20210111_0503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
