# Generated by Django 4.1.7 on 2023-02-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_copie_du_passport_post_diplome_post_diplomes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='DIPLOME',
        ),
        migrations.AlterField(
            model_name='post',
            name='COPIE_DU_PASSPORT',
            field=models.FileField(default=' ', upload_to='USERS/passport/'),
        ),
    ]
