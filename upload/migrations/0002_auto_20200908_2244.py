# Generated by Django 3.1.1 on 2020-09-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='photo',
            field=models.FileField(upload_to='files'),
        ),
    ]
