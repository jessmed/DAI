# Generated by Django 3.1.5 on 2021-01-11 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0008_auto_20210111_0501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'permissions': (('can_mark_returned', 'Hacer cambios en libros'),)},
        ),
    ]