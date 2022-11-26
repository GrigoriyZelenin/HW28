from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0004_alter_location_lat_alter_location_lng"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]