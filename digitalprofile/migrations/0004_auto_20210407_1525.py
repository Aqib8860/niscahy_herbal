# Generated by Django 3.1.4 on 2021-04-07 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digitalprofile', '0003_auto_20210407_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommerce',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentdetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialmedialinks',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='core.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='digitalprofile',
            name='company_logo',
            field=models.ImageField(blank=True, upload_to='DigitalProfile/Company/'),
        ),
    ]
