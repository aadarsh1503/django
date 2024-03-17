# Generated by Django 5.0 on 2024-03-15 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0012_burger_pizza_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_burger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=255)),
                ('receipe_descriptions', models.TextField()),
                ('receipe_image', models.ImageField(upload_to='receipe_images/')),
                ('receipe_view_count', models.IntegerField(default=1)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]