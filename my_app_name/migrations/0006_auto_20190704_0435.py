# Generated by Django 2.2.2 on 2019-07-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attrition_report', '0005_auto_20190704_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrbp',
            name='excel_reference',
            field=models.FileField(help_text='Upload Excel Reference (Note: always clean data and do not change formatting)', upload_to='HRBP'),
        ),
    ]