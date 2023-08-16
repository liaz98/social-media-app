# Generated by Django 4.0 on 2023-08-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0003_alter_user_options_alter_user_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.Post'),
        ),
    ]