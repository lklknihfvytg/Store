# Generated by Django 4.0.6 on 2022-08-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image_url1_alter_product_image_url2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url3',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
