# Generated by Django 3.1.4 on 2021-01-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hook', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_url', models.URLField(blank=True, null=True)),
                ('display', models.BooleanField(default=False)),
            ],
        ),
    ]
