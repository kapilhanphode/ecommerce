"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Ecommerce API is running 🚀"
    })


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.products.urls')),
    path('api/v1/auth/', include('apps.accounts.urls')),
    path('api/v1/cart/', include('apps.cart.urls')),
    path('api/v1/orders/', include('apps.orders.urls')),
    path('api/v1/payments/', include('apps.payments.urls')),
    path('api/v1/shipping/', include('apps.shipping.urls')),
    path('api/v1/reviews/', include('apps.reviews.urls')),
    path('api/v1/inventory/', include('apps.inventory.urls')),
    path('api/v1/analytics/', include('apps.analytics.urls')),
    path('api/v1/vendor/orders/', include('apps.vendor_orders.urls')),
    path('api/v1/wallet/', include('apps.wallet.urls')),
    path('api/v1/returns/', include('apps.returns.urls')),
]
