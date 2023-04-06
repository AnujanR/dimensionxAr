# Generated by Django 4.1.7 on 2023-04-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDate', models.DateField(auto_now=True)),
                ('uploadTime', models.TimeField(auto_now=True)),
                ('imgPath', models.CharField(max_length=265)),
                ('status', models.CharField(default='FAILED', max_length=25)),
            ],
        ),
    ]