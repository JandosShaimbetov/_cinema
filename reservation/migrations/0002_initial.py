# Generated by Django 3.2 on 2022-07-31 09:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movie", "0001_initial"),
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="reservation.discount",
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="seat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reservation.seat"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="showtime",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="movie.showtime"
            ),
        ),
        migrations.AddField(
            model_name="reservation",
            name="ticket_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reservation.tickettype"
            ),
        ),
        migrations.AddField(
            model_name="discount",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]