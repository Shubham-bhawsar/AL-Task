# Generated by Django 3.1.6 on 2021-02-05 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formdata',
            old_name='description',
            new_name='passw',
        ),
        migrations.RemoveField(
            model_name='formdata',
            name='name',
        ),
    ]
