# Generated by Django 4.2.7 on 2023-12-05 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_username_alter_comment_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
    ]
