# Generated by Django 4.0.4 on 2022-05-03 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0006_alter_ask_answer_alter_ask_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ask",
            name="answer",
            field=models.TextField(blank=True, null=True),
        ),
    ]