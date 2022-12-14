from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_rename_ing_location_lng_alter_ad_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="lat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="location",
            name="lng",
            field=models.FloatField(blank=True, null=True),
        ),
    ]