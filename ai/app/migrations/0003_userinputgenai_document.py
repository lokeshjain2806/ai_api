# Generated by Django 5.0 on 2023-12-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userinputgenai'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinputgenai',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]