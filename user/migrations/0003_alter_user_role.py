from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("member", "Участник"),
                    ("moderator", "Модератор"),
                    ("admin", "Администратор"),
                ],
                default="member",
                max_length=20,
            ),
        ),
    ]