# Generated by Django 5.1.3 on 2024-11-11 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("feastinsight", "0009_review_anthropic_theme"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="enhanced_name",
        ),
    ]
