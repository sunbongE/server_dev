# Generated by Django 3.0.5 on 2023-01-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20230112_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='user_pw',
            field=models.CharField(default=False, max_length=256),
        ),
    ]