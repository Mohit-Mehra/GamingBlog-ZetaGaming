# Generated by Django 4.1.1 on 2022-10-12 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='image',
        ),
    ]
