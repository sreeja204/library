# Generated by Django 5.1.3 on 2024-11-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_delete_popular_book_is_featured_book_is_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_offer',
            field=models.BooleanField(default=False),
        ),
    ]
