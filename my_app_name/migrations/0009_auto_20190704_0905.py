# Generated by Django 2.2.2 on 2019-07-04 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attrition_report', '0008_auto_20190704_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrbp',
            name='caf_pivot',
            field=models.ImageField(blank=True, default='tmp/caf_pivot.png', null=True, upload_to='tmp/'),
        ),
    ]