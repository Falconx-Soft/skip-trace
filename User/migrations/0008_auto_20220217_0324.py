# Generated by Django 3.2.6 on 2022-02-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20220217_0303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountscheck',
            old_name='crated_at',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='created_at',
        ),
        migrations.AddField(
            model_name='accountscheck',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
