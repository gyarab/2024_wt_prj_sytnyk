# Generated by Django 5.1.7 on 2025-03-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
