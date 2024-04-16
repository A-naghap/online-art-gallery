# Generated by Django 4.2.5 on 2023-11-06 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_competition'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='am_pm',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default=0, max_length=2),
            preserve_default=False,
        ),
    ]
