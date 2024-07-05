# Generated by Django 4.2.7 on 2023-11-10 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_farmer_user_address_user_gender_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.farmer')),
            ],
        ),
    ]