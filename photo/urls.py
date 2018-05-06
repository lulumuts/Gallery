from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url('^$',views.all_photos,name='photos'),
    url(r'^search/', views.search_photos, name='search_photos')

]
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
