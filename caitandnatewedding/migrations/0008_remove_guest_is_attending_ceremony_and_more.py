# Generated by Django 4.1 on 2022-08-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caitandnatewedding', '0007_guest_is_attending_ceremony_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='is_attending_ceremony',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='is_attending_reception',
        ),
        migrations.AddField(
            model_name='guest',
            name='is_attending',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]