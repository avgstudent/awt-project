# Generated by Django 4.1.2 on 2022-11-19 15:11

import Clinic.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocId', models.TextField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=Clinic.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('Slots', models.IntegerField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientId', models.TextField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('patientimage', models.ImageField(blank=True, null=True, upload_to=Clinic.models.get_file_path)),
                ('small_description', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('Consulatation_fee', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clinic.doctors')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
