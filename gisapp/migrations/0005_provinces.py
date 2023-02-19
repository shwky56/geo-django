# Generated by Django 4.1.7 on 2023-02-17 23:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gisapp", "0004_alter_counties_adm0_ar_alter_counties_adm0_en_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Provinces",
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
                ("adm1_en", models.CharField(max_length=50)),
                ("adm1_ar", models.CharField(max_length=50)),
                ("adm1_pcode", models.CharField(max_length=50)),
                ("adm1_ref", models.CharField(max_length=50)),
                ("adm1alt1en", models.CharField(max_length=50)),
                ("adm1alt2en", models.CharField(max_length=50)),
                ("adm1alt1ar", models.CharField(max_length=50)),
                ("adm1alt2ar", models.CharField(max_length=50)),
                ("adm0_en", models.CharField(max_length=50)),
                ("adm0_ar", models.CharField(max_length=50)),
                ("adm0_pcode", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("validon", models.DateField()),
                ("validto", models.DateField()),
                ("shape_leng", models.FloatField()),
                ("shape_area", models.FloatField()),
                (
                    "geom",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
        ),
    ]
