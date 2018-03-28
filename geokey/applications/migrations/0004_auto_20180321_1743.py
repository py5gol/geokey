# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_auto_20171024_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('deleted', 'deleted')]),
        ),
    ]
