# Generated by Django 5.1.3 on 2024-11-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("feastinsight", "0011_place_openai_enhanced_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="anthropic_enhanced_name",
            field=models.TextField(blank=True, null=True),
        ),
    ]
