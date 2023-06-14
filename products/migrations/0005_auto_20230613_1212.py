# Generated by Django 3.2.19 on 2023-06-13 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20230608_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='customizable',
        ),
        migrations.RemoveField(
            model_name='product',
            name='main_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wording_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='writing',
        ),
        migrations.CreateModel(
            name='CustomizableProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_color', models.CharField(blank=True, choices=[], max_length=50, null=True)),
                ('wording_color', models.CharField(blank=True, choices=[], max_length=50, null=True)),
                ('writing', models.CharField(blank=True, max_length=100, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]