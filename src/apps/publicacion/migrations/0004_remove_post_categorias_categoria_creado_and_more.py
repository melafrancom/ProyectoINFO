# Generated by Django 4.1 on 2022-09-01 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicacion', '0003_coment_creado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categorias',
        ),
        migrations.AddField(
            model_name='categoria',
            name='creado',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='coment',
            name='modificado',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=200, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='coment',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='coment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coments', to='publicacion.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
