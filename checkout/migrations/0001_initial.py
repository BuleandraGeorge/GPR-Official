# Generated by Django 3.1.4 on 2021-02-02 17:21

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wines', '0004_auto_20201230_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(blank=True, max_length=255, null=True)),
                ('county', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(default='RO', max_length=2)),
                ('date', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='lineitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product_size', models.CharField(max_length=10)),
                ('lineitem_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitem', to='checkout.order')),
                ('the_wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wines.wine')),
            ],
        ),
    ]
