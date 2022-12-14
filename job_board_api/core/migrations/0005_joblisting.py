# Generated by Django 4.0.5 on 2023-01-02 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_delete_joblisting'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('job_seniority', models.CharField(max_length=255)),
                ('job_description', models.TextField(blank=True)),
                ('salary_max', models.IntegerField(blank=True, default=5000, null=True)),
                ('salary_min', models.IntegerField(blank=True, default=4000, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
