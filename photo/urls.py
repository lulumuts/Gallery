from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.all_photos,name='photos'),
    url(r'^search/', views.search_photos, name='search_photos'),
    url(r'^place/',views.search_place,name='search_place'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
