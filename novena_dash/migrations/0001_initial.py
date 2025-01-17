# Generated by Django 5.1.3 on 2024-11-29 11:37

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a_users', '0002_user_about_user_confirm_password_user_is_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('doctor_pic', models.ImageField(null=True, upload_to='patient_pic')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='certificate')),
                ('descriptions', models.TextField(null=True)),
                ('skills', models.CharField(blank=True, max_length=400, null=True)),
                ('expertise_area', models.CharField(max_length=200, null=True)),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='novena_dash.departement')),
            ],
            options={
                'managed': True,
            },
            bases=('a_users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='My_Educational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100, null=True)),
                ('expertise_area', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
                ('descript', models.TextField(blank=True, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='novena_dash.doctor')),
            ],
        ),
    ]
