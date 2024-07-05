# Generated by Django 4.2.7 on 2023-11-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_farmerlandinformation_municipality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female')], default='', help_text='Select your approriate gender', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('FARMER', 'FARMER')], default='ADMIN', help_text='Required, when you select a farmer, farmer profile will automatically added.', max_length=30),
        ),
    ]
