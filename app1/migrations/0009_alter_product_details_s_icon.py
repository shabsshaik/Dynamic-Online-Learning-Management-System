# Generated by Django 4.1.7 on 2023-04-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_product_details_s_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='s_icon',
            field=models.IntegerField(max_length=50),
        ),
    ]
