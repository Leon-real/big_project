# Generated by Django 5.0 on 2024-01-02 02:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0002_client_is_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="is_approved",
        ),
    ]
