# Generated by Django 5.1.3 on 2024-11-11 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feastinsight", "0006_review_anthropic_sentiment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="theme",
        ),
    ]
