# Generated by Django 4.2.7 on 2023-12-02 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_alter_post_options_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
    ]
