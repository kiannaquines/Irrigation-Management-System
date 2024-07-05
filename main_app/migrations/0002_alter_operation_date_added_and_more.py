# Generated by Django 4.2.7 on 2023-11-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='operation_status',
            field=models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'UNAVAILABLE')], default='', max_length=155),
        ),
        migrations.AlterField(
            model_name='payment',
            name='balance',
            field=models.CharField(help_text='Required, enter here if there is a payment balance', max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.CharField(help_text='Required, enter here amount paid', max_length=255),
        ),
    ]