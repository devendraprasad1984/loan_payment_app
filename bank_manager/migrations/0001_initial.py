# Generated by Django 3.1.5 on 2021-08-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BANKS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=30, null=True, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]