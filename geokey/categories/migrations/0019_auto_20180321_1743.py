# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0018_historicalcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='colour',
            field=models.TextField(default='#0033ff'),
        ),
        migrations.AlterField(
            model_name='category',
            name='default_status',
            field=models.CharField(max_length=20, default='pending', choices=[('active', 'active'), ('pending', 'pending')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='category',
            name='symbol',
            field=models.ImageField(max_length=500, null=True, upload_to='symbols'),
        ),
        migrations.AlterField(
            model_name='field',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='colour',
            field=models.TextField(default='#0033ff'),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='default_status',
            field=models.CharField(max_length=20, default='pending', choices=[('active', 'active'), ('pending', 'pending')]),
        ),
        migrations.AlterField(
            model_name='historicalcategory',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='lookupvalue',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='lookupvalue',
            name='symbol',
            field=models.ImageField(max_length=500, null=True, upload_to='symbols'),
        ),
        migrations.AlterField(
            model_name='multiplelookupvalue',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='multiplelookupvalue',
            name='symbol',
            field=models.ImageField(max_length=500, null=True, upload_to='symbols'),
        ),
    ]
