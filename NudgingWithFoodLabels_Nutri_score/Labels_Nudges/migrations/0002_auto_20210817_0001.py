# Generated by Django 3.2.6 on 2021-08-16 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Labels_Nudges', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipes',
        ),
        migrations.AddField(
            model_name='evaluatechoices',
            name='session_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='foodcategory',
            name='session_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='session_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='selectedrecipe',
            name='session_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
