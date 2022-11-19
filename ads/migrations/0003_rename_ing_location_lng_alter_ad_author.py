from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ads", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(model_name="location", old_name="ing", new_name="lng",),
        migrations.AlterField(
            model_name="ad",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ads",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]