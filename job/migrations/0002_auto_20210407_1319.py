# Generated by Django 3.1.4 on 2021-04-07 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobseeker',
            name='extra_field',
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='company_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='experience',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='industry',
            field=models.CharField(choices=[('Accountancy', 'Accountancy'), ('Business', 'Business'), ('Charity and Voluntary Work', 'Charity and Voluntary Work'), ('Creative Arts and Design', 'Creative Arts and Design'), ('Energy and Utilities', 'Energy and Utilities'), ('Creative Arts and Design', 'Creative Arts and Design'), ('Engineering and Manufacturing', 'Engineering and Manufacturing'), ('Environment and Agriculture', 'Environment and Agriculture'), ('Healthcare', 'Healthcare'), ('Hospitality and Event Management', 'Hospitality and Event Management'), ('Information Technology', 'Information Technology'), ('Law', 'Law'), ('Leisure, Sports, and Tourism', 'Leisure, Sports, and Tourism'), ('Marketing, Advertising, and PR', 'Marketing, Advertising, and PR'), ('Media and Internet', 'Media and Internet'), ('Property and Consultation', 'Property and Consultation'), ('Public Services and Administration', 'Public Services and Administration'), ('Recruitment and HR', 'Recruitment and HR'), ('Retail', 'Retail'), ('Sales', 'Sales'), ('Science and Pharmaceuticals', 'Science and Pharmaceuticals'), ('Social Care', 'Social Care'), ('Teacher Training and Education', 'Teacher Training and Education'), ('Transport and Logistics', 'Transport and Logistics')], max_length=80),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='job_title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='requirements',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='salary_from',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='salary_to',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.user'),
        ),
        migrations.AlterField(
            model_name='jobrecruiter',
            name='your_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='job.jobrecruiter'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(upload_to='Job/Resume/'),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='status',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Selected', 'Selected'), ('Not Selected', 'Not Selected'), ('Shortlisted', 'Shortlisted')], default='Applied', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.user'),
        ),
    ]