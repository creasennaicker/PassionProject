# Generated by Django 3.1.4 on 2021-12-26 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(default='', max_length=20)),
                ('make', models.CharField(default='', max_length=20)),
                ('model', models.CharField(default='', max_length=20)),
                ('price', models.CharField(default='', max_length=20)),
                ('info', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
