# Generated by Django 2.1.2 on 2018-12-07 21:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
            options={
                'db_table': 'Coupon',
            },
        ),
    ]
