# Generated by Django 4.2.7 on 2023-11-29 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0114_remove_task_args_remove_task_kwargs"),
        ("rpm", "0057_rpmpublication_checksum_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addon",
            name="repository",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="addons",
                to="core.repository",
            ),
        ),
        migrations.AlterField(
            model_name="variant",
            name="repository",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="variants",
                to="core.repository",
            ),
        ),
    ]