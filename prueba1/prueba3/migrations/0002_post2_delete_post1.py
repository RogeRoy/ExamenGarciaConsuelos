# Generated by Django 4.1.3 on 2022-11-21 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x1', models.IntegerField(blank=True, null=True)),
                ('x2', models.CharField(blank=True, max_length=2, null=True)),
                ('x3', models.IntegerField(blank=True, null=True)),
                ('x4', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='post1',
        ),
    ]
