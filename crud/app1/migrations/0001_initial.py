# Generated by Django 5.1.4 on 2025-01-03 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.curso')),
            ],
        ),
    ]
