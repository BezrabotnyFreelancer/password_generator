# Generated by Django 4.1.1 on 2022-09-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_alter_passwordstorage_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordstorage',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]