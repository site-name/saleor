# Generated by Django 3.1.4 on 2021-01-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site", "0028_delete_authorizationkey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sitesettings",
            name="default_weight_unit",
            field=models.CharField(
                choices=[
                    ("g", "g"),
                    ("tonne", "tonne"),
                    ("oz", "oz"),
                    ("lb", "lb"),
                    ("stone", "stone"),
                    ("short_ton", "short_ton"),
                    ("long_ton", "long_ton"),
                    ("kg", "kg"),
                ],
                default="kg",
                max_length=30,
            ),
        ),
    ]
