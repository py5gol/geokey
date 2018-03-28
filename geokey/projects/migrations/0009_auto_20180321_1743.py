# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_squashed_0008_historicalproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='everyone_contributes',
            field=models.CharField(max_length=20, default='auth', choices=[('auth', 'auth'), ('false', 'false'), ('true', 'true')]),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='everyone_contributes',
            field=models.CharField(max_length=20, default='auth', choices=[('auth', 'auth'), ('false', 'false'), ('true', 'true')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
    ]
