# Generated by Django 5.1.2 on 2024-10-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_members_pythonmembers'),
    ]

    operations = [
        migrations.CreateModel(
            name='PythonMember',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('points', models.PositiveIntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='PythonMembers',
            new_name='CCharpMember',
        ),
    ]
