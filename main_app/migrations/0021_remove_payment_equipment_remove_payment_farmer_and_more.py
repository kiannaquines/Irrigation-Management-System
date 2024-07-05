# Generated by Django 4.2.7 on 2023-12-27 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_alter_reservation_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='farmer',
        ),
        migrations.AddField(
            model_name='payment',
            name='reservation',
            field=models.ForeignKey(default='', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='main_app.reservation'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.CharField(help_text="User has a balance? <a href='#' id='edit_amount'>Click here to edit</a>", max_length=255),
        ),
    ]