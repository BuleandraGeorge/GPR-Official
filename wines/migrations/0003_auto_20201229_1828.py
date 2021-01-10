# Generated by Django 3.1.4 on 2020-12-29 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0002_wine_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size_quantity_available',
            options={'verbose_name': 'Cantitate disponibila per dimensiune dimensiune', 'verbose_name_plural': 'Cantitate disponibila per dimensiune dimensiune'},
        ),
        migrations.AlterModelOptions(
            name='size_quantity_sold',
            options={'verbose_name': 'Cantitate vanduta per dimensiune dimensiune', 'verbose_name_plural': 'Cantitate vanduta per dimensiune dimensiune'},
        ),
        migrations.AlterField(
            model_name='size_quantity_available',
            name='size',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='wines.size'),
        ),
        migrations.AlterField(
            model_name='size_quantity_sold',
            name='size',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='wines.size'),
        ),
    ]