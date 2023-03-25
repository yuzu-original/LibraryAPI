# Generated by Django 4.1.7 on 2023-03-25 13:07

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_author_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона'),
        ),
    ]