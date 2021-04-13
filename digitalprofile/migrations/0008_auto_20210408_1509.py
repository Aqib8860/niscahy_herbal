# Generated by Django 3.1.4 on 2021-04-08 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitalprofile', '0007_auto_20210408_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digitalprofile',
            name='company_logo',
            field=models.ImageField(upload_to='DigitalProfile/Company/'),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='product_mrp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='product_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='ecommerce',
            name='selling_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image1',
            field=models.ImageField(upload_to='DigitalProfile/Gallery/'),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='about_us',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='designation',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='location',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='mobile',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='whatsapp',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_name1',
            field=models.CharField(max_length=50),
        ),
    ]
