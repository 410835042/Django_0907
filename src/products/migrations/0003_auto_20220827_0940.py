# Generated by Django 3.2.9 on 2022-08-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220827_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AddField(
            model_name='product',
            name='threeD_model',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
    ]
