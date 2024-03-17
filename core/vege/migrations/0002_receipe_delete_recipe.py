# Generated by Django 5.0 on 2024-01-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=255)),
                ('receipe_descriptions', models.TextField()),
                ('receipe_image', models.ImageField(upload_to='receipe_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]




