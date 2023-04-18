# Generated by Django 4.2 on 2023-04-18 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("EventixApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="event_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="EventixApp.event",
            ),
            preserve_default=False,
        ),
    ]
