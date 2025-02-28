# Generated by Django 5.1.6 on 2025-02-28 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('size', models.CharField(max_length=100)),
                ('occasion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('size', models.CharField(max_length=100)),
                ('occasion', models.CharField(max_length=100)),
            ],
        ),
    ]
