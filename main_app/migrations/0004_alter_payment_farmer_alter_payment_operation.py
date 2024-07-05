# Generated by Django 4.2.7 on 2023-11-12 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_user_gender_alter_user_role'),
        ('main_app', '0003_alter_payment_balance_alter_payment_farmer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='farmer',
            field=models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='authentication.farmer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='operation',
            field=models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='main_app.operation'),
        ),
    ]
