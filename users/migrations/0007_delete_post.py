# Generated by Django 4.1.7 on 2023-02-27 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_post_diplomes_remove_post_faculte_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
