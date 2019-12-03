# Generated by Django 2.2.7 on 2019-11-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("nubank", "0003_nubankitemsetup")]

    operations = [
        migrations.AlterField(
            model_name="nubankstatement",
            name="amount_without_iof",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True),
        )
    ]
