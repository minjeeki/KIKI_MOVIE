# Generated by Django 4.2.16 on 2024-11-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='introduce',
            field=models.TextField(null=True),
        ),
    ]
