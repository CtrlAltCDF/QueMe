# Generated by Django 4.0.4 on 2022-05-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0003_alter_ask_id_alter_customer_id_alter_question_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ask",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
