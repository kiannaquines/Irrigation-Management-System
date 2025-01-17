# Generated by Django 4.2.7 on 2023-11-12 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_user_gender_alter_user_role'),
        ('main_app', '0004_alter_payment_farmer_alter_payment_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='farmer',
            field=models.ForeignKey(default='', help_text='Required, select user here', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='authentication.farmer'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_status',
            field=models.CharField(choices=[('ONGOING OPERATION', 'ONGOING OPERATION'), ('DONE OPERATION', 'DONE OPERATION')], default='', help_text='Required, select if the operation status', max_length=155),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule_status',
            field=models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('BOOKED', 'BOOKED')], default='', help_text='Required, select schedule status here', max_length=155),
        ),
    ]
