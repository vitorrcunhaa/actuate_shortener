# Generated by Django 3.2.9 on 2021-11-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20211110_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='hash',
            field=models.CharField(default='aaa444aaaa', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
