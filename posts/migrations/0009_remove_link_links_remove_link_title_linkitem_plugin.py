# Generated by Django 5.1.2 on 2024-12-16 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0008_linkitem_remove_link_link_remove_link_text_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="link",
            name="links",
        ),
        migrations.RemoveField(
            model_name="link",
            name="title",
        ),
        migrations.AddField(
            model_name="linkitem",
            name="plugin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="link_items",
                to="posts.link",
            ),
        ),
    ]