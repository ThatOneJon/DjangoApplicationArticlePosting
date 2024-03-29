# Generated by Django 4.0.6 on 2022-09-06 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalBlog', '0002_userprofile_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='Your bio here...', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profileName',
            field=models.CharField(blank=True, default='John Doe', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
