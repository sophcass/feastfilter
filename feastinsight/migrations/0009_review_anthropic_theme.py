# Generated by Django 5.1.3 on 2024-11-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feastinsight", "0008_review_openai_theme"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="anthropic_theme",
            field=models.TextField(blank=True, null=True),
        ),
    ]