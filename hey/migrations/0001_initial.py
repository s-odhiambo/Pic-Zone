# Generated by Django 3.0 on 2019-12-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default=0, upload_to='images/')),
                ('category_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hey.Category')),
                ('location_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hey.Location')),
            ],
        ),
    ]
