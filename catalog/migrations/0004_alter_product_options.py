# Generated by Django 4.2 on 2024-10-04 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
    ]
