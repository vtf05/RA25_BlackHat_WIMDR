# Generated by Django 3.0.8 on 2020-08-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_accident'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='accident',
            field=models.IntegerField(default=0),
        ),
    ]
