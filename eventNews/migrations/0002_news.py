# Generated by Django 4.0.5 on 2023-08-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventNews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
    ]