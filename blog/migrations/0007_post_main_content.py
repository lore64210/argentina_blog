# Generated by Django 4.2.1 on 2023-10-30 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_admin_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_content',
            field=models.BooleanField(default=False),
        ),
    ]