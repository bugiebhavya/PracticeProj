# Generated by Django 3.0.8 on 2020-07-28 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200723_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='sponsor',
        ),
        migrations.DeleteModel(
            name='Sponsor',
        ),
    ]
