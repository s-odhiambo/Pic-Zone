# Generated by Django 3.0 on 2019-12-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hey', '0005_auto_20191215_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=' integer', upload_to='images/'),
        ),
    ]
