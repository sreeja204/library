# Generated by Django 5.1.3 on 2024-11-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
