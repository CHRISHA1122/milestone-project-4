# Generated by Django 3.2.19 on 2023-06-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230607_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customizable',
            field=models.BooleanField(default=False),
        ),
    ]
