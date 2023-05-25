"""
URL configuration for HW_django_month4 project.

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
from django.urls import path
from django.conf.urls.static import static

from posts.views import main_view, products_view, product_detail_view, product_create_view
from HW_django_month4 import settings


"""

CLIENT →  http://localhost:8000/admin/ 
→ DJANGO admin/ in urlpatterns 
DJANGO → admin_view(HttpRequest)
admin_view(HttpRequest) → HttResponse('Django Admin Panel')

"""

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_view),

    path('products/', products_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', product_create_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)