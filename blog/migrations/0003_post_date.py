# Generated by Django 4.1.6 on 2023-02-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_excerpt_post_excerpt_post_author_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]