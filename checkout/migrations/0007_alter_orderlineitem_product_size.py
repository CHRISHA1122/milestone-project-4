# Generated by Django 3.2.19 on 2023-07-04 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20230704_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_size',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]