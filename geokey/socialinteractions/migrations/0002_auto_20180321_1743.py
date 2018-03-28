# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialinteractions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialinteractionpost',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive')]),
        ),
        migrations.AlterField(
            model_name='socialinteractionpull',
            name='frequency',
            field=models.CharField(max_length=20, default='daily', choices=[('5min', '5min'), ('10min', '10min'), ('20min', '20min'), ('30min', '30min'), ('hourly', 'hourly'), ('daily', 'daily'), ('weekly', 'weekly'), ('fortnightly', 'fortnightly'), ('monthly', 'monthly')]),
        ),
        migrations.AlterField(
            model_name='socialinteractionpull',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive')]),
        ),
    ]
