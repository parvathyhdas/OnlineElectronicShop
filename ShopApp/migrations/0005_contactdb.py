# Generated by Django 4.2.5 on 2023-10-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0004_productdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Message', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
