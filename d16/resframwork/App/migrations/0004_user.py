# Generated by Django 2.0 on 2019-10-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=32, unique=True)),
                ('u_password', models.CharField(max_length=100)),
            ],
        ),
    ]
