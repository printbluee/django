from django.contrib import admin
from django.urls import path, include
#from pybo import views
from pybo.views_folder import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('pybo/',include('pybo.urls')),
#     path('common/', include('common.urls')),
#     path('', views.index, name='index'),  # '/' 에 해당되는 path
# ] # pybo/로 시작하는 페이지를 요청하면 이제 pybo/urls.py 파일의 매핑 정보를 읽어서 처리하라는 의미
