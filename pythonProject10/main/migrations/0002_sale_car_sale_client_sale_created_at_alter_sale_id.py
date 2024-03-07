# Generated by Django 5.0.3 on 2024-03-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='car',
            field=models.ManyToManyField(to='main.car'),
        ),
        migrations.AddField(
            model_name='sale',
            name='client',
            field=models.ManyToManyField(to='main.client'),
        ),
        migrations.AddField(
            model_name='sale',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]