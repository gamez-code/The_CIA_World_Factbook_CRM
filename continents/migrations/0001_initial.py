# Generated by Django 2.0.2 on 2018-03-04 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('translation', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=8)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
    ]
