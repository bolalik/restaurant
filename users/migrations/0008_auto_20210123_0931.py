# Generated by Django 3.1.5 on 2021-01-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210123_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'admin')], default=''),
        ),
    ]
