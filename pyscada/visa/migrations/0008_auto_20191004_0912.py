# Generated by Django 2.2.6 on 2019-10-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visa', '0007_auto_20171219_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visadevice',
            name='instrument',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visa.VISADeviceHandler'),
        ),
    ]