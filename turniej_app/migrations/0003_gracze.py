# Generated by Django 3.0.7 on 2020-06-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turniej_app', '0002_auto_20200620_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gracze',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
    ]
