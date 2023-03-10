# Generated by Django 4.1.7 on 2023-02-19 05:53

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctermapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="County",
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
                ("code", models.CharField(max_length=50, unique=True)),
                ("geom", django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name="Street",
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
                ("lode", models.IntegerField(default=0)),
                ("description", models.TextField(max_length=1000)),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.LineStringField(srid=4326),
                ),
            ],
        ),
    ]
