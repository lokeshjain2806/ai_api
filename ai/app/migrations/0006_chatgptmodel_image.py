# Generated by Django 5.0 on 2024-01-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_chatgptmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgptmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
