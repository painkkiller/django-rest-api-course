# Generated by Django 3.0.3 on 2020-02-22 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingregients',
            new_name='ingredients',
        ),
    ]