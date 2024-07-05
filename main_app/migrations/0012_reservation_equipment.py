# Generated by Django 4.2.7 on 2023-12-02 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='equipment',
            field=models.ForeignKey(default='', help_text='Select equipment for operation.', null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.equipment'),
        ),
    ]