# Generated by Django 4.1.1 on 2022-09-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordstorage',
            name='key',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
