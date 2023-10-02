from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Online_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('product/', include("product.urls")),
    path('cart/', include("cart.urls")),
    path('', include("home.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
