from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        verbose_name = "سایز"
        verbose_name_plural = "سایز"

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        verbose_name = "رنگ"
        verbose_name_plural = "رنگ ها"

    def __str__(self):
        return self.title


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subs', verbose_name='دسته بزرگ')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField()

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    discount = models.SmallIntegerField(verbose_name="تخفیف")
    image = models.ImageField(upload_to="products", verbose_name="تصویر")
    size = models.ManyToManyField(Size, blank=True, null=True, related_name='products', verbose_name="سایز")
    color = models.ManyToManyField(Color, related_name='products', verbose_name="رنگ")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title


class Information(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name="informations", verbose_name='محصول')
    text = models.TextField(verbose_name='اطلاعات')

    class Meta:
        verbose_name = "اطلاعات"
        verbose_name_plural = "اطلاعات"


