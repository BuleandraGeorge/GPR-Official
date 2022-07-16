# Generated by Django 4.0.6 on 2022-07-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_postcode',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='default_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]