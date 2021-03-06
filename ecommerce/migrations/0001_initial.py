# Generated by Django 3.1.4 on 2021-04-20 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=80)),
                ('product_image1', models.ImageField(blank=True, null=True, upload_to='Ecommerce/Products')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='Ecommerce/Products')),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to='Ecommerce/Products')),
                ('product_image4', models.ImageField(blank=True, null=True, upload_to='Ecommerce/Products')),
                ('product_image5', models.ImageField(blank=True, null=True, upload_to='Ecommerce/Products')),
                ('product_mrp', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('in_stock', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Nischay Herbal Products',
            },
        ),
        migrations.CreateModel(
            name='RatingReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Rating & Reviews',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
