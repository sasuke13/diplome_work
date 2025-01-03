# Generated by Django 5.1.2 on 2024-12-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_link"),
    ]

    operations = [
        migrations.CreateModel(
            name="LinkItem",
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
                ("text", models.CharField(max_length=255, verbose_name="Link Text")),
                ("url", models.URLField(verbose_name="URL")),
                ("order", models.PositiveIntegerField(default=0, verbose_name="Order")),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.RemoveField(
            model_name="link",
            name="link",
        ),
        migrations.RemoveField(
            model_name="link",
            name="text",
        ),
        migrations.AddField(
            model_name="link",
            name="title",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Section Title"
            ),
        ),
        migrations.AddField(
            model_name="link",
            name="links",
            field=models.ManyToManyField(
                related_name="link_plugins", to="posts.linkitem"
            ),
        ),
    ]
