# Generated by Django 4.2.7 on 2023-12-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='title',
            new_name='url',
        ),
    ]
