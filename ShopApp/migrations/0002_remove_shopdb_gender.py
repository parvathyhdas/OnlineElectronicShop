# Generated by Django 4.2.5 on 2023-09-26 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopdb',
            name='Gender',
        ),
    ]
