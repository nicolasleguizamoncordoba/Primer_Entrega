# Generated by Django 4.1.2 on 2022-10-23 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombremascota', models.CharField(max_length=100)),
                ('tipomascota', models.CharField(max_length=100)),
                ('edadmascota', models.IntegerField()),
                ('dueñomascota', models.CharField(max_length=100)),
            ],
        ),
    ]
