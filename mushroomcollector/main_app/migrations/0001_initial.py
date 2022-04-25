# Generated by Django 4.0.4 on 2022-04-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mushroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('season', models.CharField(max_length=100)),
                ('edibility', models.CharField(max_length=100)),
            ],
        ),
    ]
