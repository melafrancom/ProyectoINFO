# Generated by Django 4.1 on 2022-08-16 01:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0002_alter_post_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
