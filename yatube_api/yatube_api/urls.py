from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('posts.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'

    ),
]
