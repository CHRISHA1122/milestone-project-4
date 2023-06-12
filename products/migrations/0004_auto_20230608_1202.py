# Generated by Django 3.2.19 on 2023-06-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_customizable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_color',
            field=models.CharField(blank=True, choices=[], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='wording_color',
            field=models.CharField(blank=True, choices=[], max_length=50, null=True),
        ),
    ]