# Generated by Django 3.1.7 on 2021-03-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0017_auto_20210323_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkmodel',
            name='short_link',
        ),
        migrations.AddField(
            model_name='linkmodel',
            name='slug',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
