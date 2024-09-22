# Generated by Django 5.1 on 2024-09-22 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_version_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='versions', to='catalog.product', verbose_name='Название продукта'),
        ),
    ]
