# Generated by Django 5.1.1 on 2024-10-03 22:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='user',
            new_name='user_id',
        ),
    ]
