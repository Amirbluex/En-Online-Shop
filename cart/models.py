from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='مشتری')
    total_price = models.IntegerField(default=0, verbose_name='قیمت کل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد شده')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')

    def __str__(self):
        return self.user.phone_number

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = "سفارشات"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pr_items', verbose_name='محصول')
    size = models.CharField(max_length=12, verbose_name='سایز')
    color = models.CharField(max_length=20, verbose_name='رنگ')
    quantity = models.SmallIntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت')

    def __str__(self):
        return self.order.user.phone_number

    class Meta:
        verbose_name = "آیتم سبد خرید"
        verbose_name_plural = 'آیتم های سبد خرید'


class DiscountCode(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='کد')
    discount = models.SmallIntegerField(default=0, verbose_name='میزان تخفیف')
    quantity = models.SmallIntegerField(default=1, verbose_name="تعداد")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = 'کد های تخفیف'
