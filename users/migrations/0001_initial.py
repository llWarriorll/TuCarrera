# Generated by Django 5.0.6 on 2024-07-03 00:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=50)),
                ('curp', models.CharField(max_length=18)),
                ('municipio', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('bachillerato', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
