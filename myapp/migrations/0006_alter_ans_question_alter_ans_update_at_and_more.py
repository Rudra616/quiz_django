# Generated by Django 5.1.4 on 2025-01-07 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_rename_answer_ans"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ans",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answers",
                to="myapp.question",
            ),
        ),
        migrations.AlterField(
            model_name="ans",
            name="update_at",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="update_at",
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="question",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="myapp.category",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="update_at",
            field=models.DateField(auto_now=True),
        ),
    ]