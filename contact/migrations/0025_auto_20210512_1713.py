# Generated by Django 3.1.8 on 2021-05-12 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0024_auto_20210511_1130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['title'], 'verbose_name_plural': 'people'},
        ),
    ]
