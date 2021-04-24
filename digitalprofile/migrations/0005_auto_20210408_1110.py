# Generated by Django 3.1.4 on 2021-04-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalprofile', '0004_auto_20210407_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='digitalprofile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='about_us',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='designation',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='email',
            field=models.EmailField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='location',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='mobile',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]