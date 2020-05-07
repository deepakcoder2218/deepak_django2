# Generated by Django 3.0.5 on 2020-05-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_cat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='shop/images/company'),
        ),
    ]