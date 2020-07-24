# Generated by Django 3.0.8 on 2020-07-23 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('topic', models.CharField(max_length=50, verbose_name='Topic')),
                ('start_date', models.TimeField(verbose_name='Start')),
                ('end_date', models.TimeField(verbose_name='End')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='Company Name')),
                ('person_in_contact', models.CharField(max_length=50, verbose_name='Contact Person')),
                ('event', models.ManyToManyField(to='home.Event', verbose_name='Event')),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
        ),
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Time')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Event', verbose_name='Event')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Sponsor', verbose_name='Sponsor')),
            ],
            options={
                'verbose_name': 'Event Detail',
                'verbose_name_plural': 'Event Details',
            },
        ),
    ]