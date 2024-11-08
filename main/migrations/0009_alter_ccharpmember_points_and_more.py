# Generated by Django 5.1.2 on 2024-11-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_ccharpmember_collage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccharpmember',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='graphicdesginmember',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pythonmember',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]