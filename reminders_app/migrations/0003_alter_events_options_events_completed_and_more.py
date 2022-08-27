# Generated by Django 4.1 on 2022-08-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders_app', '0002_events_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='events',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='events',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
