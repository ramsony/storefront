# Generated by Django 4.0.1 on 2022-02-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.CharField(default='1916 Saginaw DR', max_length=255),
        ),
    ]