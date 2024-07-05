# Generated by Django 4.2.7 on 2023-11-14 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_reservation_confirmation_alter_payment_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='confirmation',
            field=models.CharField(choices=[('NOT CONFIRM', 'NOT CONFIRM'), ('CONFIRMED', 'CONFIRMED')], default='NOT CONFIRM', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='schedule_id',
            field=models.ForeignKey(default='', help_text='Required, select schedule here. If empty no available schedule.', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='main_app.schedule'),
        ),
    ]