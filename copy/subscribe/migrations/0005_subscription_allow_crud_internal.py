# Generated by Django 3.2.6 on 2021-08-23 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_subscription_allow_external'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='allow_crud_internal',
            field=models.BooleanField(default=False),
        ),
    ]