# Generated by Django 4.1.7 on 2023-04-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_username', models.CharField(max_length=50)),
                ('Customer_email', models.EmailField(max_length=50)),
                ('Customer_password', models.CharField(max_length=50)),
            ],
        ),
    ]