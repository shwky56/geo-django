# Generated by Django 4.1.6 on 2023-02-19 02:30

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gisapp", "0008_alter_strite_f_code_des_alter_strite_geom_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Strite2",
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
                ("type", models.CharField(max_length=22)),
                ("name", models.CharField(max_length=113)),
                ("oneway", models.CharField(max_length=17)),
                ("lanes", models.BigIntegerField()),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326),
                ),
            ],
        ),
    ]
