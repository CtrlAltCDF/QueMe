# Generated by Django 4.0.4 on 2022-05-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0004_alter_ask_id_alter_customer_id_alter_question_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ask",
            name="answer",
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name="ask",
            name="status",
            field=models.TextField(default=None),
        ),
    ]
