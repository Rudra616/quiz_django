# Generated by Django 5.1.4 on 2025-01-05 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_rename_is_correct_answer_iscorrect"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Answer",
            new_name="Ans",
        ),
    ]
