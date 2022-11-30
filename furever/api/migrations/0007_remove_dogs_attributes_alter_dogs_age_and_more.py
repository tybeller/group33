# Generated by Django 4.1.2 on 2022-11-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_dogs_images_alter_dogs_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dogs',
            name='attributes',
        ),
        migrations.AlterField(
            model_name='dogs',
            name='age',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='breed',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='sex',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='weight',
            field=models.CharField(default='', max_length=3),
        ),
    ]
