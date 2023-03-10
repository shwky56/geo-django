# Generated by Django 4.1.7 on 2023-02-19 05:44

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctore",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Hosptall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                ("street_name", models.CharField(max_length=500)),
                ("location", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("doctores", models.ManyToManyField(to="doctermapp.doctore")),
            ],
        ),
    ]
