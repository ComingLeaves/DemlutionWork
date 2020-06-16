# Generated by Django 3.0 on 2020-06-13 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
                ('nickname', models.CharField(default='匿名', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
