# Generated by Django 4.2.7 on 2023-11-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_botanical_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
