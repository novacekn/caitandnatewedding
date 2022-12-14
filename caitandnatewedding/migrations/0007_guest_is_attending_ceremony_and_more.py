# Generated by Django 4.1 on 2022-08-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caitandnatewedding', '0006_alter_guest_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='is_attending_ceremony',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='is_attending_reception',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='household',
            name='state',
            field=models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY'), ('ON', 'ON')], max_length=2),
        ),
    ]
