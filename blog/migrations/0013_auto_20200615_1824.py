# Generated by Django 3.0 on 2020-06-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200615_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='completed',
            field=models.IntegerField(max_length=10),
        ),
    ]
