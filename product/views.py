from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from product.models import Product, Category


class ProductDetailView(DetailView):
    template_name = "product/product_detail.html"
    model = Product


class NavbarPartialView(TemplateView):
    template_name = 'includes/nav_bar.html'

    def get_context_data(self, **kwargs):
        context = super(NavbarPartialView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
