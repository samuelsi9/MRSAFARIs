# Generated by Django 4.1.7 on 2023-02-27 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_diplome_alter_post_copie_du_passport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='NATIONALITE',
            new_name='PAYS',
        ),
    ]
