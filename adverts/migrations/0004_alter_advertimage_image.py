# Generated by Django 3.2.4 on 2021-06-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0003_auto_20210622_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertimage',
            name='image',
            field=models.ImageField(upload_to='adverts/'),
        ),
    ]
