# Generated by Django 3.1.1 on 2020-12-20 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='cutomer',
            new_name='customer',
        ),
    ]