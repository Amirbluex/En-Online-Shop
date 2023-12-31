# Generated by Django 4.2 on 2023-06-05 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='آدرس ایمبل')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد شده')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='مشتری')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=12, verbose_name='سایز')),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('quantity', models.SmallIntegerField(verbose_name='تعداد')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order', verbose_name='سفارش')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_items', to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'آیتم سبد خرید',
                'verbose_name_plural': 'آیتم های سبد خرید',
            },
        ),
    ]
