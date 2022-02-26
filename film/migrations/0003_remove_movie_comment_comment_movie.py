# Generated by Django 4.0 on 2022-01-22 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_comment_movie_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='film.movie'),
        ),
    ]
