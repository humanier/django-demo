# Generated by Django 5.0.6 on 2024-05-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]