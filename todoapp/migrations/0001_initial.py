# Generated by Django 4.2.6 on 2023-10-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=250)),
                ('is_item_complate', models.BooleanField(default=False)),
                ('create_at', models.TimeField(auto_now_add=True)),
                ('update_at', models.TimeField(auto_now=True)),
            ],
        ),
    ]
