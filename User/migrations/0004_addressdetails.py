# Generated by Django 3.2.6 on 2022-02-16 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20220217_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='addressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
    ]
