# Generated by Django 3.1.1 on 2020-09-26 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/', verbose_name='Image')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('caption', models.CharField(blank=True, max_length=50, verbose_name='Caption')),
                ('location', models.CharField(blank=True, max_length=30, verbose_name='Location')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owner', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL)),
                ('saves', models.ManyToManyField(blank=True, related_name='Saves', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, related_name='Tagged_Users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
