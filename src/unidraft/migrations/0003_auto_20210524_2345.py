# Generated by Django 3.2.3 on 2021-05-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidraft', '0002_rename_user_myuserclass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuserclass',
            name='user',
        ),
        migrations.AlterField(
            model_name='myuserclass',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]