# Generated by Django 4.2 on 2023-06-06 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_otp_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='نام کامل')),
                ('address', models.CharField(max_length=400, verbose_name='آدرس')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='آدرس ایمبل')),
                ('phone', models.CharField(max_length=11, verbose_name='تلفن همراه')),
                ('postal_code', models.CharField(max_length=10, verbose_name='کد پستی')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='informations', to=settings.AUTH_USER_MODEL, verbose_name='مشتری')),
            ],
        ),
    ]
