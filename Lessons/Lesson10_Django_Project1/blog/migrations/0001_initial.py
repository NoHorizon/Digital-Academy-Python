# Generated by Django 4.2.2 on 2023-06-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
