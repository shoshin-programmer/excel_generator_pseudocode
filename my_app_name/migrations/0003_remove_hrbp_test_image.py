# Generated by Django 2.2.2 on 2019-07-02 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attrition_report', '0002_auto_20190629_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hrbp',
            name='test_image',
        ),
    ]
