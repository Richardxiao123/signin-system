# Generated by Django 4.2.1 on 2023-09-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=20)),
                ('cPhone', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
