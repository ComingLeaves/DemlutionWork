# Generated by Django 3.0 on 2020-06-15 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200615_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='completed',
            field=models.CharField(max_length=5),
        ),
    ]
