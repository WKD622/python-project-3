# Generated by Django 2.0.6 on 2018-06-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20180615_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]