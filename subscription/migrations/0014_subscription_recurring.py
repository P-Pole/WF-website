# Generated by Django 3.0.7 on 2020-07-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0013_remove_subscription_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='recurring',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]