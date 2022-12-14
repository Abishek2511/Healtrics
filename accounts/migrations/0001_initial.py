# Generated by Django 3.2 on 2022-10-30 05:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email_address', models.EmailField(max_length=500, unique=True)),
                ('mobile_number', models.TextField(unique=True)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Hospital', 'Hospital'), ('Blood Bank', 'Blood Bank'), ('Donor', 'Donor')], default='Admin', max_length=500)),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('email_code', models.CharField(max_length=10, null=True)),
                ('mobile_code', models.CharField(max_length=10, null=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_mobile_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
