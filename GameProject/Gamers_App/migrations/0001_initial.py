# Generated by Django 3.0.5 on 2020-05-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
            ],
        ),
    ]
