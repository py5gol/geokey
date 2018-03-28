# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0018_historicalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='audio',
            field=models.FileField(upload_to='user-uploads/audio'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='review_status',
            field=models.CharField(max_length=10, blank=True, null=True, choices=[('open', 'open'), ('resolved', 'resolved')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='historicalcomment',
            name='review_status',
            field=models.CharField(max_length=10, blank=True, null=True, choices=[('open', 'open'), ('resolved', 'resolved')]),
        ),
        migrations.AlterField(
            model_name='historicalcomment',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='historicalobservation',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('draft', 'draft'), ('review', 'review'), ('pending', 'pending'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(upload_to='user-uploads/images'),
        ),
        migrations.AlterField(
            model_name='location',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('review', 'review')]),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='observation',
            name='status',
            field=models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('draft', 'draft'), ('review', 'review'), ('pending', 'pending'), ('deleted', 'deleted')]),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='user-uploads/videos'),
        ),
        migrations.AlterField(
            model_name='videofile',
            name='video',
            field=models.ImageField(upload_to='user-uploads/videos'),
        ),
    ]
