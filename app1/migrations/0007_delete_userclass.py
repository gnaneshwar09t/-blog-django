# Generated by Django 4.2.8 on 2023-12-30 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_userclass_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userclass',
        ),
    ]