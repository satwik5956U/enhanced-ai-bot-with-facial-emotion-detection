# Generated by Django 4.1.7 on 2024-03-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=255)),
                ('by', models.CharField(max_length=4)),
                ('chat', models.CharField(max_length=255)),
            ],
        ),
    ]