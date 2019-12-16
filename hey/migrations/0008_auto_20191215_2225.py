# Generated by Django 3.0 on 2019-12-15 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hey', '0007_auto_20191215_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='DEFAULT VALUE', on_delete=django.db.models.deletion.CASCADE, to='hey.Location'),
        ),
    ]
