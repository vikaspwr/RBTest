# Generated by Django 2.2 on 2020-07-07 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApplicationTest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
