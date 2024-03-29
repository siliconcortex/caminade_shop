# Generated by Django 3.1 on 2020-08-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='shop/thumbnails'),
        ),
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=models.ImageField(null=True, upload_to='shop/main_images'),
        ),
    ]
