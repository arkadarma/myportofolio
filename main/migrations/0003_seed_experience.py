import sys

from django.db import migrations


def create_experience(apps, schema_editor):
    if "test" in sys.argv:
        return

    Experience = apps.get_model("main", "Experience")

    Experience.objects.get_or_create(
        title="Staff BEM Fasilkom UI - Departemen Olahraga",
        defaults={
            "description": "Staff BEM Fasilkom UI pada Departemen Olahraga.",
            "category": "full-time",
            "thumbnail": None,
            "ended_at": None,
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_project"),
    ]

    operations = [
        migrations.RunPython(create_experience),
    ]