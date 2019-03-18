from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^photo/(\d+)', views.single_photo, name='singlePhoto'),
    url(r'^$', views.all_images, name='allImages'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^search_locations/(\w+)', views.search_locations, name='search_locations'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
