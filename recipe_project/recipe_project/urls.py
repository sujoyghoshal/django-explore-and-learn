from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from vegi.views import receipes, delete_recipe

urlpatterns = [
    path('', receipes, name='receipes'),
    path('delete/<int:id>/', delete_recipe, name='delete_recipe'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
