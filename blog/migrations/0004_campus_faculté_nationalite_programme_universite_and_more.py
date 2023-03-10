# Generated by Django 4.1.7 on 2023-02-27 17:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_postnom'),
    ]

    operations = [
        migrations.CreateModel(
            name='CAMPUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='faculté',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculténom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NATIONALITE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NATIONNOM', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PROGRAMME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROGRAMMENOM', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UNIVERSITE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UNIVERSITENOM', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='NUMERO_DE_TEL',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='FACULTE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.faculté'),
        ),
        migrations.AddField(
            model_name='post',
            name='LOGEMENT',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.campus'),
        ),
        migrations.AddField(
            model_name='post',
            name='NATIONALITE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.nationalite'),
        ),
        migrations.AddField(
            model_name='post',
            name='PROGRAMME',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.programme'),
        ),
        migrations.AddField(
            model_name='post',
            name='UNIVERSITE',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.universite'),
        ),
    ]
