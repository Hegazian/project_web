# Generated by Django 3.1 on 2021-06-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symname', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'symptom',
                'verbose_name_plural': 'symptoms',
            },
        ),
    ]
