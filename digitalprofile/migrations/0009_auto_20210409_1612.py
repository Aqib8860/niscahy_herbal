# Generated by Django 3.1.4 on 2021-04-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalprofile', '0008_auto_20210408_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]