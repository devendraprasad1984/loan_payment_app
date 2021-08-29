# Generated by Django 3.1.5 on 2021-08-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUBSCRIPTION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('secret_key', models.TextField(null=True)),
                ('signer', models.TextField(null=True)),
                ('allow_external', models.BooleanField(default=False)),
                ('allow_crud_internal', models.BooleanField(default=False)),
                ('type', models.CharField(default='manager', max_length=50, null=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]