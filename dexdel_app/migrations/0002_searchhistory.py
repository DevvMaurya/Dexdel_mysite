# Generated by Django 5.0 on 2024-01-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dexdel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ask', models.CharField(max_length=255)),
            ],
        ),
    ]
