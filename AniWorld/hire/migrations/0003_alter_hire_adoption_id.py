# Generated by Django 3.2.3 on 2021-05-14 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_remove_hire_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='adoption_id',
            field=models.IntegerField(default=0),
        ),
    ]
