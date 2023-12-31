# Generated by Django 4.2 on 2023-06-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_userinformation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinformation',
            options={'verbose_name': 'اطلاعات کاربر', 'verbose_name_plural': 'اطلاعات کاربرها'},
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='آدرس ایمیل'),
        ),
    ]
