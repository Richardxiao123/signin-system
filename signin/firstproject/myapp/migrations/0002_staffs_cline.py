# Generated by Django 4.2.1 on 2023-09-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='cLine',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
