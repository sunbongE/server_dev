# Generated by Django 3.0.5 on 2023-01-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='이름'),
        ),
    ]
