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

from posts.views import MainPageCBV, ProductsCBV, ProductDetailCBV, product_create_view
from HW_django_month4 import settings

from users.views import register_view, login_view, logout_view

"""

CLIENT →  http://localhost:8000/admin/ 
→ DJANGO admin/ in urlpatterns 
DJANGO → admin_view(HttpRequest)
admin_view(HttpRequest) → HttResponse('Django Admin Panel')

"""

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', MainPageCBV.as_view()),

    path('products/', ProductsCBV.as_view()),
    path('products/<int:id>/', ProductsCBV.as_view()),
    path('products/create/', product_create_view),

    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)