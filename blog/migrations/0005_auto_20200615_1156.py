# Generated by Django 3.0 on 2020-06-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_todos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
