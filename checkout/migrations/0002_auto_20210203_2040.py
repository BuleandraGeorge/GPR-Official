# Generated by Django 3.1.4 on 2021-02-03 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line_1',
            new_name='adresa',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line_2',
            new_name='adresa_linia_2',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='county',
            new_name='judet',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='nume',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='country',
            new_name='tara',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone_number',
            new_name='telefon',
        ),
    ]
