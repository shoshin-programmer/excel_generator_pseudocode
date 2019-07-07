# Generated by Django 2.2.2 on 2019-07-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attrition_report', '0007_hrbp_caf_pivot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrbp',
            name='caf_pivot',
            field=models.ImageField(blank=True, default='caf_pivot.png', null=True, upload_to='tmp/'),
        ),
        migrations.AlterField(
            model_name='hrbp',
            name='excel_reference',
            field=models.FileField(help_text='Upload Excel Reference (Note: always clean data and do not change formatting)', upload_to='HRBP/'),
        ),
    ]
